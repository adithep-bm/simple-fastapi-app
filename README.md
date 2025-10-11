# FastAPI Clean Code Example

โปรเจค FastAPI ตัวอย่างสำหรับ CI/CD Pipeline ด้วย Jenkins, Docker และ SonarQube

## 📋 สารบัญ

- [คำอธิบายโปรเจค](#คำอธิบายโปรเจค)
- [คุณสมบัติ](#คุณสมบัติ)
- [เทคโนโลยีที่ใช้](#เทคโนโลยีที่ใช้)
- [การติดตั้ง](#การติดตั้ง)
- [การรันโปรเจค](#การรันโปรเจค)
- [การทดสอบ](#การทดสอบ)
- [API Documentation](#api-documentation)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [โครงสร้างโปรเจค](#โครงสร้างโปรเจค)

## 🎯 คำอธิบายโปรเจค

นี่คือโปรเจค FastAPI สำหรับสาธิตการใช้งาน CI/CD Pipeline แบบครบวงจร โดยมีการเชื่อมต่อกับ:

- **Jenkins**: สำหรับ Continuous Integration และ Deployment
- **Docker**: สำหรับการ containerization
- **SonarQube**: สำหรับการตรวจสอบคุณภาพโค้ด
- **pytest**: สำหรับการทดสอบอัตโนมัติและ code coverage

## ✨ คุณสมบัติ

- REST API endpoints สำหรับ:
  - คำนวณค่าเฉลี่ย (average)
  - กลับลำดับข้อความ (reverse string)
- Unit Tests พร้อม Code Coverage
- Docker containerization
- Jenkins Pipeline อัตโนมัติ
- การตรวจสอบคุณภาพโค้ดด้วย SonarQube

## 🛠 เทคโนโลยีที่ใช้

- **Python 3.11**
- **FastAPI 0.111.0** - Modern web framework
- **Uvicorn 0.30.0** - ASGI server
- **Pytest 8.2.0** - Testing framework
- **pytest-cov 5.0.0** - Code coverage plugin
- **Docker** - Containerization
- **Jenkins** - CI/CD automation
- **SonarQube** - Code quality analysis

## 📦 การติดตั้ง

### Prerequisites

- Python 3.11 หรือสูงกว่า
- pip
- virtualenv (แนะนำ)

### ขั้นตอนการติดตั้ง

1. Clone repository

```bash
git clone https://github.com/adithep-bm/simple-fastapi-app.git
cd simple-fastapi-app
```

2. สร้าง Virtual Environment

```bash
python -m venv fastapi-env
```

3. Activate Virtual Environment

**Windows (PowerShell):**

```powershell
.\fastapi-env\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
source fastapi-env/bin/activate
```

4. ติดตั้ง dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🚀 การรันโปรเจค

### รันแบบ Local Development

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

เปิดเบราว์เซอร์และเข้าไปที่:

- API: http://localhost:8000
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## 🧪 การทดสอบ

### รัน Unit Tests

```bash
pytest
```

### รัน Tests พร้อม Coverage Report

```bash
pytest --cov=app --cov-report=html --cov-report=xml
```

Coverage report จะถูกสร้างใน:

- HTML: `htmlcov/index.html`
- XML: `coverage.xml` (สำหรับ SonarQube)

### รัน Tests แบบละเอียด

```bash
pytest -v --disable-warnings
```

## 📚 API Documentation

### Endpoints

#### 1. Root Endpoint

**GET** `/`

ตรวจสอบสถานะของ API

**Response:**

```json
{
  "message": "Hello from FastAPI with Jenkins & SonarQube!"
}
```

#### 2. Calculate Average

**GET** `/average`

คำนวณค่าเฉลี่ยจากรายการตัวเลข

**Query Parameters:**

- `numbers` (required): List ของตัวเลข (สามารถส่งหลายค่าได้)

**Example Request:**

```bash
curl "http://localhost:8000/average?numbers=10&numbers=20&numbers=30"
```

**Response:**

```json
{
  "average": 20.0
}
```

**Error Response (400):**

```json
{
  "detail": "Numbers list must not be empty"
}
```

#### 3. Reverse String

**GET** `/reverse`

กลับลำดับข้อความ

**Query Parameters:**

- `text` (required): ข้อความที่ต้องการกลับลำดับ

**Example Request:**

```bash
curl "http://localhost:8000/reverse?text=SonarQube"
```

**Response:**

```json
{
  "reversed": "ebuQranoS"
}
```

## 🐳 Docker

### Build Docker Image

```bash
docker build -t fastapi-app:latest .
```

### Run Docker Container

```bash
docker run -d --name fastapi-app -p 8000:8000 fastapi-app:latest
```

### Stop และ Remove Container

```bash
docker stop fastapi-app
docker rm fastapi-app
```

### ดู Logs

```bash
docker logs fastapi-app
```

## 🔄 CI/CD Pipeline

โปรเจคนี้ใช้ Jenkins Pipeline (`Jenkinsfile`) ที่ประกอบด้วย stages ต่อไปนี้:

### Pipeline Stages

1. **Checkout**: ดึงโค้ดจาก Git repository
2. **Install Java 17**: ติดตั้ง Java สำหรับ SonarQube Scanner
3. **Install docker CLI**: ติดตั้ง Docker CLI สำหรับการ build image
4. **Setup venv**: สร้าง Python virtual environment และติดตั้ง dependencies
5. **Run Tests & Coverage**: รัน pytest พร้อมสร้าง coverage report
6. **SonarQube Analysis**: วิเคราะห์คุณภาพโค้ดด้วย SonarQube
7. **Build Docker Image**: Build Docker image
8. **Deploy Container**: Deploy container ไปยัง environment

### SonarQube Configuration

ดูการตั้งค่าใน `sonar-project.properties`:

```properties
sonar.projectKey=fastapi
sonar.projectName=FastAPI Clean Demo
sonar.sources=app
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
```

## 📁 โครงสร้างโปรเจค

```
simple-fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application และ endpoints
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Unit tests
├── fastapi-env/             # Virtual environment
├── Dockerfile               # Docker configuration
├── Jenkinsfile              # Jenkins pipeline configuration
├── requirements.txt         # Python dependencies
├── sonar-project.properties # SonarQube configuration
├── coverage.xml             # Coverage report (generated)
└── README.md                # Project documentation
```

## 📊 Code Coverage

Current code coverage: **88%**

ดู detailed coverage report:

```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes.

## 👤 Author

- **GitHub**: [@adithep-bm](https://github.com/adithep-bm)

## 🔗 Links

- Repository: https://github.com/adithep-bm/simple-fastapi-app
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Jenkins Documentation: https://www.jenkins.io/doc/
- SonarQube Documentation: https://docs.sonarqube.org/

## 📞 Support

หากมีปัญหาหรือข้อสงสัย กรุณาเปิด [GitHub Issue](https://github.com/adithep-bm/simple-fastapi-app/issues)

---

Made with ❤️ using FastAPI
