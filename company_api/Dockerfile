FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install gunicorn==20.1.0
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT [ "sh", "entrypoint.sh" ]
