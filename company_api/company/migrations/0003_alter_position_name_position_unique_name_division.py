# Generated by Django 5.0 on 2023-12-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_employee_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название должности'),
        ),
        migrations.AddConstraint(
            model_name='position',
            constraint=models.UniqueConstraint(fields=('name', 'division'), name='unique_name_division'),
        ),
    ]
