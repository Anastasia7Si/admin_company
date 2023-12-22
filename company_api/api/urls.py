from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DivisionViewSet, EmployeeViewSet,
                    OrganizationViewSet, PermissionViewSet,
                    PositionViewSet)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('organization',
                   OrganizationViewSet,
                   basename='organization'
                   )
router_v1.register('division', DivisionViewSet, basename='division')
router_v1.register('position', PositionViewSet, basename='position')
router_v1.register('permission', PermissionViewSet, basename='permission')
router_v1.register('employee', EmployeeViewSet, basename='employee')


urlpatterns = [
    path('', include(router_v1.urls)),
]
