from django.db import models


class Organization(models.Model):
    """Класс организации."""
    name = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name='Название организации'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class Division(models.Model):
    """Класс подразделения."""
    name = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name='Название подразделения'
        )
    related_division = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Связанное подразделение'
        )
    organization = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Организация'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        constraints = [
            models.UniqueConstraint(fields=['name', 'related_division'],
                                    name='unique_name_related_division')
        ]

    def __str__(self):
        return self.name


class Position(models.Model):
    """Класс должности."""
    name = models.CharField(
        max_length=100,
        verbose_name='Название должности'
        )
    division = models.ForeignKey(
        Division,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Подразделение'
        )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        constraints = [
            models.UniqueConstraint(fields=['name', 'division'],
                                    name='unique_name_division')
        ]

    def __str__(self):
        return self.name


class Permission(models.Model):
    """Класс прав согласно должности."""
    name = models.CharField(
        max_length=50,
        verbose_name='Право'
        )
    positions = models.ManyToManyField(
        Position,
        through='PositionPermission',
        verbose_name='Позиции',
        related_name='permissions'
        )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Право'
        verbose_name_plural = 'Права'

    def __str__(self):
        return self.name


class PositionPermission(models.Model):
    """Класс для связи Position и Permission."""
    position = models.ForeignKey(
        Position,
        related_name='position_permissions',
        on_delete=models.CASCADE
        )
    permission = models.ForeignKey(
        Permission,
        related_name='position_permissions',
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('position',)
        verbose_name = 'Должностное право'
        verbose_name_plural = 'Должностные права'

    def __str__(self):
        return f'{self.position} - {self.permission}'


class Employee(models.Model):
    """Класс сотрудника."""
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя сотрудника'
        )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия сотрудника'
        )
    position = models.ManyToManyField(
        Position,
        through='EmployeePosition',
        verbose_name='Позиция сотрудника',
        related_name='employees'
        )
    organization = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Организация'
    )

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmployeePosition(models.Model):
    """Класс для связи Employee и Position."""
    employee = models.ForeignKey(
        Employee,
        related_name='employee_positions',
        on_delete=models.CASCADE
        )
    position = models.ForeignKey(
        Position,
        related_name='employee_positions',
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('position',)
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'

    def __str__(self):
        return f'{self.employee} - {self.position}'
