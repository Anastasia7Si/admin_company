import csv
import sqlite3 as sql

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка данных из csv-файлов в базу данных'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Загрузка данных началась')
        )
        conn = sql.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT * FROM company_division")
        with open("company_division.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_employee")
        with open("company_employee.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_employeeposition")
        with open("company_employeeposition.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_organization")
        with open("company_organization.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_permission")
        with open("company_permission.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_position")
        with open("company_position.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        c.execute("SELECT * FROM company_positionpermission")
        with open("company_positionpermission.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        conn.close()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
