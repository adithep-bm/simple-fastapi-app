pipeline {
  agent {
    docker {
      image 'python:3.11'
      // เมานต์ docker.sock เพื่อคุยกับ daemon ภายนอก
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  stages {
    stage('Install docker CLI in agent') {
      steps {
        sh '''
          set -eux
          apt-get update
          apt-get install -y ca-certificates curl gnupg lsb-release
          install -m 0755 -d /etc/apt/keyrings
          curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
          echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
          apt-get update
          apt-get install -y docker-ce-cli
          docker version
        '''
      }
    }

    stage('Checkout') { steps { git branch: 'main', url: 'https://github.com/adithep-bm/simple-fastapi-app.git' } }

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
          export PYTHONPATH="$WORKSPACE:${PYTHONPATH}"
          fastapi-env/bin/pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml
        '''
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('Sonarqube') {
          sh '''
            docker run --rm \
              -e SONAR_HOST_URL="$SONAR_HOST_URL" \
              -e SONAR_LOGIN="$SONAR_AUTH_TOKEN" \
              -v "$PWD:/usr/src" \
              sonarsource/sonar-scanner-cli:latest
          '''
        }
      }
    }

    stage('Build Docker Image') { steps { sh 'docker build -t fastapi-app:latest .' } }
    stage('Deploy Container') {
      steps {
        sh '''
          docker rm -f fastapi-app || true
          docker run -d --name fastapi-app -p 8000:8000 fastapi-app:latest
        '''
      }
    }
  }
}
