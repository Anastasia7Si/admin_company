from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from company.models import (Division, Employee, Organization,
                            Permission, Position)
from .serializers import (DivisionSerializer, EmployeeSerializer,
                          OrganizationSerializer, PermissionSerializer,
                          PositionSerializer)


class OrganizationViewSet(ReadOnlyModelViewSet):
    """Вьюсет организации."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DivisionViewSet(ModelViewSet):
    """Вьюсет подразделений."""
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class PositionViewSet(ModelViewSet):
    """Вьюсет должностей."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PermissionViewSet(ModelViewSet):
    """Вьюсет прав."""
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class EmployeeViewSet(ModelViewSet):
    """Вьюсет сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
