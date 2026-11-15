pipeline {
    agent any

    environment {
        PYTHON = 'python3.10'
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Setup Python 3.10 venv') {
            steps {
                sh '''
                    $PYTHON --version
                    $PYTHON -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=reports/test-results.xml
                '''
            }
            post {
                always { junit 'reports/test-results.xml' }
            }
        }

        stage('Evidently Report') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m monitoring.drift_report
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}