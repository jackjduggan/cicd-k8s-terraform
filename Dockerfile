FROM python:3

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install pip dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project over
COPY . .

# debug
RUN ls -l .

WORKDIR /app/project_tracker/project_tracker

# debug
RUN ls -l /app/project_tracker/project_tracker 

# RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project_tracker.wsgi:application"]