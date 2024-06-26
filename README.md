# cicd-k8s-terraform

The objective of this project is to learn about a handful of relevant skills by combining them all into one project. \
I will look to build a CI/CD pipeline for a Python web application using Jenkins. The pipeline will include automated testing, Docker containerization, K8s deployment, and IaC provisioning with Terraform.

**Work Done**
- Set up python virtual environment 
    - `pip install virtualenv`
    - `cd <project_directory>`
    - `python -m venv venv`
    - `venv\Scripts\activate`

- Built basic Python Django app: Project Tracker
    - `pip install django`
    - `django-admin startproject project_tracker`
    - `cd project_tracker`
    - `python manage.py startapp projects`
    - Added `projects` to `INSTALLED_APPS` in `settings.py`
    - Created project model in `projects/models.py`
    - Created an applied migrations:
        - `python manage.py makemigrations`
        - `python manage.py migrate`
    - Defined views in `projects/views.py`
    - Created URL patterns in `projects.py`, one for home page, one for project details page.
    - Created html page templates in `projects/templates/<page_name>.html`
    - Created administrator interface in `projects/admin.py`
    - Created superuser, and ran server to access admin interface and add projects
        - `python manage.py createsuperuser`
        - `python manage.py runserver`
        - **INSERT IMAGES OF WEB APP**
    - Wrote basic tests for project creation

- Set up Jenkins
    - Created an AWS EC2 instance and installed Jenkins on it
        - On the EC2 instance:
            - `sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key`
            - `echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null`
            - `sudo apt-get update`
            - `sudo apt-get install fontconfig openjdk-17-jre`
            - `sudo apt-get install jenkins`
        - To test if the Jenkins service is running, use:
            - `sudo systemctl status jenkins.service`
            - **INSERT IMAGE OF COMMAND OUTPUT**
        - Visit `<ip_address>:8080/` and unlock Jenkins with `initialAdminPassword`.
        - Install suggested Jenkins plugins
        - Created first Admin user
        - **INSERT IMAGE OF JENKINS DASHBOARD**
        - In `Manage Jenkins` > `Plugins` > `Available Plugins`, install:
            - Github Integration
            - Docker
            - Pipeline (may already be installed)
            - Docker Pipeline
            - Kubernetes
            - Blue Ocean
        - In `Manage Jenkins` > `Tools`, set up Git and Docker
        - Set up a new Jenkins Pipeline Job.
        
        