pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dvggan/django-project"
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Choutout') {
            steps {
                git 'https://github.com/jackjduggan/cicd-k8s-terraform.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker_image = docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker_image.inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "${REGISTRY_CREDENTIALS}") {
                        docker_image.push("${env.BUILD_ID}")
                        docker_image.push("latest")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}