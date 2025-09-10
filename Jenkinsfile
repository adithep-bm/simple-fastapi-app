pipeline {
    agent {
        docker {
            image 'openjdk:11-jdk'
            args '-v /var/run/docker.sock:/var/run/docker.sock -u root'
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

        stage('Setup Environment (Python)') {
            steps {
                sh '''
                echo "===== Checking User and Permissions ====="
                whoami
                id
                
                echo "===== Installing Python ====="
                # Create missing directories and fix permissions
                mkdir -p /var/lib/apt/lists/partial
                mkdir -p /var/cache/apt/archives/partial
                
                # Update package list and install Python
                apt-get update
                apt-get install -y python3 python3-pip python3-venv curl unzip

                echo "===== Setting up Python Virtual Environment ====="
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt

                echo "===== Installing SonarQube Scanner ====="
                curl -L --output sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                unzip sonar-scanner-cli.zip
                mv sonar-scanner-4.8.0.2856-linux /opt/sonar-scanner
                ln -sf /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner

                echo "===== Verification ====="
                java -version
                python3 --version
                sonar-scanner --version
                . venv/bin/activate && python -c "import sys; print(sys.version)"
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                echo "===== Running Tests ====="
                . venv/bin/activate
                pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonarqube') { // Ensure 'Sonarqube' matches Jenkins config
                    sh '''
                    echo "===== Running SonarQube Analysis ====="
                    # Ensure Python venv is active
                    . venv/bin/activate
                    # Run Sonar Scanner CLI
                    sonar-scanner
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                 // Ensure Docker commands run on the *host* using the mounted socket
                sh '''
                echo "===== Building Docker Image ====="
                docker build -t fastapi-app:latest .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                echo "===== Deploying Container ====="
                # Stop and remove previous container if it exists
                docker stop fastapi-app-container || true
                docker rm fastapi-app-container || true
                # Run the new container
                docker run -d --name fastapi-app-container -p 8000:8000 fastapi-app:latest
                '''
            }
        }

         stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred', // Ensure this matches Jenkins credential ID
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "===== Pushing to Docker Registry ====="
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    # Tag the image correctly for Docker Hub
                    docker tag fastapi-app:latest $DOCKER_USER/fastapi-app:latest
                    docker push $DOCKER_USER/fastapi-app:latest
                    # Optional: Logout
                    # docker logout
                    '''
                }
            }
        }

    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
