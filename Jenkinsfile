pipeline {
    agent any

    environment {
        IMAGE_NAME = "salman1930/two-tier-flask-app:latest"
        BACKEND_CONTAINER = "two-tier-flask-app-backend-1"
        MYSQL_CONTAINER = "two-tier-flask-app-mysql-1"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '===== Checking out source code ====='
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                echo '===== Building Flask Image ====='
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Deploy Stack') {
            steps {
                echo '===== Deploying Flask & MySQL via Docker Compose ====='
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '===== Verifying Services ====='
                sh 'docker compose ps'
                sh 'docker logs --tail 30 ${BACKEND_CONTAINER} || docker compose logs backend'
            }
        }
    }

    post {
        success {
            echo '===== DEPLOYMENT SUCCESSFUL ====='
        }
        failure {
            echo '===== DEPLOYMENT FAILED ====='
        }
    }
}
