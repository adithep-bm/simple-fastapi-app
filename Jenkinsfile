pipeline {
    agent {
        docker {
            image 'python:3.11'     // Docker image ที่ต้องการใช้
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // optional ถ้าต้องใช้ Docker CLI
        }
    }
    environment {
        SONARQUBE = credentials('sonarqube_token')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/adithep-bm/simple-fastapi-app.git'
            }
        }
        stage('Install SonarQube Scanner') {
            steps {
                sh '''
                apt-get update && apt-get install -y wget unzip openjdk-17-jre-headless
                cd /tmp
                wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-7.2.0.5079-linux-x64.zip
                unzip sonar-scanner-cli-7.2.0.5079-linux-x64.zip
                mv sonar-scanner-7.2.0.5079-linux-x64 /opt/sonar-scanner
                ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                export HOME=/tmp/jenkins_home
                mkdir -p $HOME/.local/bin
                export PATH=$HOME/.local/bin:$PATH
                export PYTHONUSERBASE=$HOME/.local
                python -m pip install --user --upgrade pip
                python -m pip install --user -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests & Coverage') {
            steps {
                sh '''
                export HOME=/tmp/jenkins_home
                export PATH=$HOME/.local/bin:$PATH
                export PYTHONUSERBASE=$HOME/.local
                python -m pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonarqube') {
                    sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=fastapi \
                        -Dsonar.projectName=FastAPI-App \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=app \
                        -Dsonar.sourceEncoding=UTF-8 \
                        -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 8000:8000 fastapi-app:latest'
            }
        }
    }
    post {
        always {
            echo "Pipeline finished"
        }
    }
}
