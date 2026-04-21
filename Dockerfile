FROM python:3.11

WORKDIR /app

COPY ./sportcore /app

RUN pip install django djangorestframework requests

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]