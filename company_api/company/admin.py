from django.contrib import admin

from .models import (Division, Employee, EmployeePosition, Organization,
                     Permission, Position, PositionPermission)


class PositionPermissionInline(admin.TabularInline):
    model = PositionPermission
    min_num = 1


class EmployeePositionInline(admin.TabularInline):
    model = EmployeePosition
    min_num = 1


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'related_division', 'organization')
    list_filter = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeePositionInline,)
    list_display = ('first_name', 'last_name', 'organization')
    list_filter = ('last_name', 'position')


@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'position')
    list_filter = ('employee', 'position')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_positions')
    list_filter = ('name', 'positions')

    def display_positions(self, obj):
        return ', '.join([position.name for position in obj.positions.all()])
    display_positions.short_description = 'Должности'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')
    list_filter = ('name', 'division')


@admin.register(PositionPermission)
class PositionPermissionAdmin(admin.ModelAdmin):
    list_display = ('position', 'permission')
    list_filter = ('position', 'permission')
