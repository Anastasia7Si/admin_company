# Generated by Django 5.0 on 2023-12-24 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_division_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positionpermission',
            options={'ordering': ('position',), 'verbose_name': 'Должностное право', 'verbose_name_plural': 'Должностные права'},
        ),
    ]
