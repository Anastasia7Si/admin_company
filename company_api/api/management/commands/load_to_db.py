from csv import DictReader

from django.core.management.base import BaseCommand

from company.models import (Division, Employee, EmployeePosition,
                            Organization, Permission, Position,
                            PositionPermission)


class Command(BaseCommand):
    help = 'Загрузка данных из csv-файлов в базу данных'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Загрузка данных началась')
        )

        for row in DictReader(
            open('db_date/company_organization.csv',
                 encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            organization = Organization(
                id=row['id'],
                name=row['name']
            )
            organization.save()

        for row in DictReader(
            open('db_date/company_division.csv', encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            if row['related_division_id'] == '':
                related_division_id = None
            else:
                related_division_id = Division.objects.get(
                    pk=row['related_division_id']
                    )
            division = Division(
                id=row['id'],
                name=row['name'],
                organization=Organization.objects.get(
                    pk=row['organization_id']
                    ),
                related_division=related_division_id
            )
            division.save()

        for row in DictReader(
            open('db_date/company_employee.csv', encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            employee = Employee(
                id=row['id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                organization=Organization.objects.get(
                    pk=row['organization_id']
                    )
            )
            employee.save()

        for row in DictReader(
            open('db_date/company_position.csv', encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            position = Position(
                id=row['id'],
                name=row['name'],
                division=Division.objects.get(pk=row['division_id'])
            )
            position.save()

        for row in DictReader(
            open('db_date/company_employeeposition.csv',
                 encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            employee_position = EmployeePosition(
                id=row['id'],
                employee=Employee.objects.get(
                    pk=row['employee_id']
                    ),
                position=Position.objects.get(pk=row['position_id'])
            )
            employee_position.save()

        for row in DictReader(
            open('db_date/company_permission.csv',
                 encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            permission = Permission(
                id=row['id'],
                name=row['name']
            )
            permission.save()

        for row in DictReader(
            open('db_date/company_positionpermission.csv',
                 encoding='utf-8', mode='r'),
            delimiter=';', escapechar='\\'
        ):
            position_permission = PositionPermission(
                id=row['id'],
                permission=Permission.objects.get(
                    pk=row['permission_id']
                    ),
                position=Position.objects.get(pk=row['position_id'])
            )
            position_permission.save()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
