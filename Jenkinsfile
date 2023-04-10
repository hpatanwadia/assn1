pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/hpatanwadia/assn2.git']]])
            }
        }
        
        stage('Build and Deploy') {
            environment {
                NODE_HOME = tool 'NodeJS'
                PHP_HOME = tool 'PHP'
                FLASK_APP = 'index.html'
            }
            steps {
                script {
                    if (fileExists('package.json')) {
                        sh 'npm install'
                        sh 'npm run build'
                        sh 'npm run start'
                    } else if (fileExists('index.html')) {
                        sh 'php index.php'
                    } else if (fileExists('index.html')) {
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
