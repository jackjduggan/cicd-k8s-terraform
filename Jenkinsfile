pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dvggan/django-project"
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jackjduggan/cicd-k8s-terraform.git'
                script {
                    echo "Workspace directory: ${WORKSPACE}"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside("-v ${WORKSPACE}:/app -w /app/project_tracker") {
                        sh 'ls -la /app'
                        sh 'ls -la /app/project_tracker'
                        sh 'python manage.py test'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "${REGISTRY_CREDENTIALS}") {
                        dockerImage.push("${env.BUILD_ID}")
                        dockerImage.push("latest")
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
