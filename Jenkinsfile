
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python 3.10 venv') {
            steps {
                bat '''
                    py -3.10 --version
                    py -3.10 -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pytest -v
                '''
            }
        }

        stage('Evidently Report') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe monitor.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.html',
                allowEmptyArchive: true
        }

        success {
            echo 'MLOps Pipeline executed successfully!'
        }

        failure {
            echo 'MLOps Pipeline execution failed!'
        }
    }
}
