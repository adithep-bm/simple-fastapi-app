pipeline {
    agent {
        docker {
            image 'openjdk:11-jdk'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
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
                echo "===== Setting up Python Virtual Environment ====="
                # Use system python3 or the one available in the Jenkins image
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt

                # Verify installations
                . venv/bin/activate && python -c "import sys; print(sys.version)"
                . venv/bin/activate && pip list
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
                    # Ensure Java is available
                    java -version
                    which java
                    # Ensure Python venv is active if sonar-scanner needs specific packages
                    . venv/bin/activate
                    # Run Sonar Scanner CLI (ensure it's installed in the Jenkins image or install it here)
                    # If sonar-scanner is not installed globally, you might need to download it or install via pip
                    # Example installing sonar-scanner CLI (uncomment if needed):
                    # curl -L --output sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                    # unzip sonar-scanner-cli.zip
                    # export PATH=$PWD/sonar-scanner-4.8.0.2856-linux/bin:$PATH

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
