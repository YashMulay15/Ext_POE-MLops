
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
            "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version

            "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv .venv

            if errorlevel 1 exit /b 1

            .venv\\Scripts\\python.exe -m pip install --upgrade pip

            if errorlevel 1 exit /b 1

            .venv\\Scripts\\python.exe -m pip install -r requirements.txt

            if errorlevel 1 exit /b 1
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
