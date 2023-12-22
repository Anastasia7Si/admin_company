from rest_framework import serializers

from company.models import (Division, Employee, EmployeePosition, Organization,
                            Permission, Position, PositionPermission)


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор организации."""
    class Meta:
        model = Organization
        fields = ('id', 'name')


class DivisionReadSerializer(serializers.ModelSerializer):
    """Сериализатор подразделения."""
    related_division = serializers.StringRelatedField()
    organization = serializers.CharField(source='organization.name')

    class Meta:
        model = Division
        fields = ('name', 'related_division', 'organization')


class DivisionSerializer(serializers.ModelSerializer):
    """Сериализатор подразделения."""
    class Meta:
        model = Division
        fields = ('id', 'name', 'related_division', 'organization')

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return DivisionReadSerializer(instance, context=context).data


class PositionPermissionSerializer(serializers.ModelSerializer):
    """Сериализатор прав должности."""

    class Meta:
        model = PositionPermission
        fields = ('id', 'position', 'permission')


class PositionReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра должности."""
    division = serializers.StringRelatedField()

    class Meta:
        model = Position
        fields = ('name', 'division')


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор должности."""

    class Meta:
        model = Position
        fields = ('id', 'name', 'division')

    def create(self, validated_data):
        position = Position.objects.create(**validated_data)
        return position

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PositionReadSerializer(instance, context=context).data


class PermissionReadSerializer(serializers.ModelSerializer):
    """Сериализатор прав."""
    positions = PositionReadSerializer(many=True)

    class Meta:
        model = Permission
        fields = ('name', 'positions')


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
        position_name = obj.position.first().name
        division_name = obj.position.first().division.name
        return f'{position_name} - {division_name}'


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор создания сотрудника."""
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all()
    )

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'organization')

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        employee = Employee.objects.create(**validated_data)
        position = Position.objects.get(id=position_data.id)
        EmployeePosition.objects.create(
            position=position, employee=employee
        )
        employee.position.add(position)
        return employee

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return EmployeeReadSerializer(instance, context=context).data
