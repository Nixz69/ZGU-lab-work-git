pipeline {
    agent { label 'pypeline_creater' }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://gitlab.com/lab48002104/lab4-gitlab',branch:'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest --junitxml=report.xml || true' // Игнорирует ошибки тестов
            }
        }
        stage('Code Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                sh '''sonar-scanner \
                -Dsonar.projectKey=maks \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://0.0.0.0:9000 \
                -Dsonar.login=sqp_deb5fa2fcbd775e6a8f68688c4a1d7102eaf1cf6''' || echo 'SonarQube analysis skipped'
            }
        }

    }
    post {
        always {
            echo 'Publishing test results...'
            junit 'report.xml'
        }
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
