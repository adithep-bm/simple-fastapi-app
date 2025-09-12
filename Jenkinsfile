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
        stage('Setup venv') {
            steps {
                sh '''
                python3 -m venv fastapi-env
                . fastapi-env/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests & Coverage') {
            steps {
                sh '''
                fastapi-env/bin/pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml
                '''
            }
        }
        stage('Install SonarQube Scanner') {
            steps {
                sh '''
                # ติดตั้ง SonarQube Scanner
                apt-get update
                apt-get install -y wget unzip
                wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                unzip sonar-scanner-cli-4.8.0.2856-linux.zip -d /tmp/
                mv /tmp/sonar-scanner-4.8.0.2856-linux /tmp/sonar-scanner
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonarqube') {
                    sh '''
                    export PATH=/tmp/sonar-scanner/bin:$PATH
                    sonar-scanner
                    '''
                }
            }
        }

        stage('Install Docker CLI') {
            steps {
                sh '''
                # ติดตั้ง Docker CLI
                apt-get update
                apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
                curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
                echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
                apt-get update
                apt-get install -y docker-ce-cli
                '''
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
