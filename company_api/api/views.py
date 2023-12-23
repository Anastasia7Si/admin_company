from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from company.models import (Division, Employee, Organization,
                            Permission, Position)
from .serializers import (DivisionSerializer, EmployeeSerializer,
                          OrganizationSerializer, PermissionSerializer,
                          PositionSerializer)


class OrganizationViewSet(ModelViewSet):
    """Вьюсет организации."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DivisionViewSet(ModelViewSet):
    """Вьюсет подразделений."""
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


class PositionViewSet(ModelViewSet):
    """Вьюсет должностей."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


class PermissionViewSet(ModelViewSet):
    """Вьюсет прав."""
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'positions')


class EmployeeViewSet(ModelViewSet):
    """Вьюсет сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('last_name', 'position')
    search_fields = ('last_name',)
