pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/YOUR_REPO_URL.git']]])
            }
        }
        
        stage('Build and Deploy') {
            environment {
                NODE_HOME = tool 'NodeJS'
                PHP_HOME = tool 'PHP'
                FLASK_APP = 'app.py'
            }
            steps {
                script {
                    if (fileExists('package.json')) {
                        sh 'npm install'
                        sh 'npm run build'
                        sh 'npm run start'
                    } else if (fileExists('index.php')) {
                        sh 'php index.php'
                    } else if (fileExists('app.py')) {
                        sh 'pip install -r requirements.txt'
                        sh 'flask run'
                    } else {
                        error 'No supported files found!'
                    }
                }
            }
        }
    }
}
