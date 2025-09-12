pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    options { timestamps() }

    // environment {
        // ไม่ต้องกำหนด token เอง ถ้าใช้ withSonarQubeEnv
        // SONARQUBE = credentials('sonarqube_token')
        // (ลบทิ้งได้)
    // }

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
                  # กันปัญหา import app ไม่ได้
                  export PYTHONPATH="$WORKSPACE:${PYTHONPATH}"
                  fastapi-env/bin/pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: '**/junit*.xml'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonarqube') {
                sh """
                    "${tool 'SonarScanner'}/bin/sonar-scanner" \
                    -Dsonar.projectKey=fastapi \
                    -Dsonar.sources=app \
                    -Dsonar.tests=tests \
                    -Dsonar.python.coverage.reportPaths=coverage.xml
                """
                }
            }
        }


        // (ถ้าตั้ง Webhook ระหว่าง SonarQube -> Jenkins แล้ว ค่อยเปิดสเตจนี้)
        // stage('Quality Gate') {
        //     steps {
        //         timeout(time: 10, unit: 'MINUTES') {
        //             waitForQualityGate abortPipeline: true
        //         }
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                  # หยุด/ลบคอนเทนเนอร์เก่าถ้ามี เพื่อลดพอร์ตชน
                  docker rm -f fastapi-app || true
                  docker run -d --name fastapi-app -p 8000:8000 fastapi-app:latest
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
