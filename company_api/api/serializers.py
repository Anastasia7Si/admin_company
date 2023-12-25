from rest_framework import serializers

from company.models import (Division, Employee, EmployeePosition, Organization,
                            Permission, Position, PositionPermission)


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор организации."""
    class Meta:
        model = Organization
        fields = ('id', 'name')


class DivisionReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра подразделения."""
    related_division = serializers.StringRelatedField()
    organization = serializers.CharField(source='organization.name')

    class Meta:
        model = Division
        fields = ('name', 'related_division', 'organization')


class DivisionSerializer(serializers.ModelSerializer):
    """Сериализатор создания подразделения."""
    class Meta:
        model = Division
        fields = ('id', 'name', 'related_division', 'organization')

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return DivisionReadSerializer(instance, context=context).data


class PositionPermissionSerializer(serializers.ModelSerializer):
    """Сериализатор создания прав должности."""
    class Meta:
        model = PositionPermission
        fields = ('id', 'position', 'permission')


class PositionReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра должности."""
    division = serializers.SerializerMethodField()

    class Meta:
        model = Position
        fields = ('name', 'division')

    def get_division(self, obj):
        return obj.division.name


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор создания должности."""
    class Meta:
        model = Position
        fields = ('id', 'name', 'division')

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PositionReadSerializer(instance, context=context).data


class PermissionReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра прав."""
    positions = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = ('name', 'positions')

    def get_positions(self, obj):
        positions = obj.positions.all()
        serializer = PositionReadSerializer(positions, many=True)
        return serializer.data


class PermissionSerializer(serializers.ModelSerializer):
    """Сериализатор создания прав."""
    positions = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all()
    )

    class Meta:
        model = Permission
        fields = ('id', 'name', 'positions')

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        permission = Permission.objects.create(name=validated_data['name'])
        position = Position.objects.get(id=positions_data.id)
        PositionPermission.objects.create(
            position=position, permission=permission
            )
        return permission

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PermissionReadSerializer(instance, context=context).data


class EmployeeReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра сотрудника."""
    position = serializers.SerializerMethodField()
    organization = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'organization')

    def get_position(self, obj):
        positions = obj.position.all().values('name', 'division__name')
        return positions


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор создания сотрудника."""
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        many=False
    )

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'organization')

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        try:
            employee = Employee.objects.get(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
        except Employee.DoesNotExist:
            employee = Employee.objects.create(**validated_data)
        position = Position.objects.get(id=position_data.id)
        EmployeePosition.objects.create(
            position=position, employee=employee
        )
        employee.position.add(position)
        return employee

    def update(self, instance, validated_data):
        all_positions = instance.position.all()
        updated_position = validated_data.pop('position')
        instance.first_name = validated_data.get(
            'first_name', instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name
            )
        instance.save()

        if updated_position:
            if updated_position in all_positions:
                instance.position.remove(updated_position)
            else:
                instance.position.add(updated_position)
        return instance

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return EmployeeReadSerializer(instance, context=context).data
