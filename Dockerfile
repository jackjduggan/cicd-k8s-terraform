FROM python:3

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

RUN ls -l /app

WORKDIR /app/project_tracker/project_tracker

# Debug
RUN ls -l /app/project_tracker/project_tracker 

# RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project_tracker.wsgi:application"]