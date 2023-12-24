# admin_company
Тестовое задание для Placebo/25

Приложение для управления структурой компании и правами сотрудников.

### Как запустить проект локально:
- Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:Anastasia7Si/admin_company.git
cd admin_company
```
- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Cоздать .env файл и внести в него свои данные, например:
```
DJANGO_SECRET_KEY= 'django-insecure-example-seckret-key'
```
- Создание супер-пользователя:
```
python manage.py createsuperuser
```
- Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
- При необходимости загрузки/выгрузки тестовых данных(находятся в папке db_date) выполнить команды:
```
python manage.py load_to_db
python manage.py load_to_csv
```
- Запустить проект (доступ по адресу http://127.0.0.1:8000/api/):
```
python manage.py runserver
```
- К проекту подключен Swagger, в котором можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/swagger/
```
- Админка доступна по адресу:
```
http://127.0.0.1:8000/admin/
```

### Как запустить проект в контейнерах (доступ по http://localhost:80/api/)
- Для работы в контейнерах проект необходимо настроить для работы с PostgreSQL: дополнить .env-файл данными, согласно примеру и изменить настройки:
```
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db_name
DB_PORT=db_port
DB_HOST=db_host_name
```
```
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', ''),
        'NAME': os.getenv('DB_NAME', ''),
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', '')
    }
}
```
- Запустить сборку  проекта:
```
docker-compose up -d
```