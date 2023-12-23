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
- Запустить проект:
```
python manage.py runserver
```
- К проекту подключен Swagger, в котором можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/swagger/
```
