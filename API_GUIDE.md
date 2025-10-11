# API Usage Guide

คู่มือการใช้งาน API อย่างละเอียด

## 📖 สารบัญ

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Error Handling](#error-handling)
- [Examples](#examples)

## 🚀 Getting Started

### Base URL

เมื่อรันในโหมด development:

```
http://localhost:8000
```

เมื่อ deploy บน production:

```
https://your-domain.com
```

### Interactive Documentation

FastAPI มี interactive API documentation สำเร็จรูป:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔐 Authentication

โปรเจคนี้ยังไม่มีการใช้งาน authentication ในเวอร์ชันปัจจุบัน สามารถเพิ่มได้โดยใช้:

- JWT (JSON Web Tokens)
- OAuth2
- API Keys

## 📍 Endpoints

### 1. Health Check

ตรวจสอบว่า API ทำงานปกติหรือไม่

```http
GET /
```

**Response 200 OK**

```json
{
  "message": "Hello from FastAPI with Jenkins & SonarQube!"
}
```

**cURL Example:**

```bash
curl http://localhost:8000/
```

**Python Example:**

```python
import requests

response = requests.get("http://localhost:8000/")
print(response.json())
```

---

### 2. Calculate Average

คำนวณค่าเฉลี่ยจากรายการตัวเลข

```http
GET /average?numbers={num1}&numbers={num2}&...
```

**Query Parameters:**

| Parameter | Type  | Required | Description                        |
| --------- | ----- | -------- | ---------------------------------- |
| numbers   | float | Yes      | รายการตัวเลข (สามารถส่งหลายค่าได้) |

**Success Response 200 OK**

```json
{
  "average": 20.0
}
```

**Error Response 400 Bad Request**

```json
{
  "detail": "Numbers list must not be empty"
}
```

**Error Response 422 Unprocessable Entity**

```json
{
  "detail": [
    {
      "loc": ["query", "numbers"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Examples:**

**cURL:**

```bash
# คำนวณค่าเฉลี่ยของ 10, 20, 30
curl "http://localhost:8000/average?numbers=10&numbers=20&numbers=30"

# คำนวณค่าเฉลี่ยของทศนิยม
curl "http://localhost:8000/average?numbers=1.5&numbers=2.5&numbers=3.0"
```

**Python:**

```python
import requests

# Single request
response = requests.get(
    "http://localhost:8000/average",
    params={"numbers": [10, 20, 30]}
)
print(response.json())  # {"average": 20.0}

# Using httpx
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get(
        "http://localhost:8000/average",
        params={"numbers": [15, 25, 35]}
    )
    print(response.json())  # {"average": 25.0}
```

**JavaScript:**

```javascript
// Using fetch API
const numbers = [10, 20, 30];
const queryString = numbers.map((n) => `numbers=${n}`).join("&");

fetch(`http://localhost:8000/average?${queryString}`)
  .then((response) => response.json())
  .then((data) => console.log(data));

// Using axios
const axios = require("axios");

axios
  .get("http://localhost:8000/average", {
    params: {
      numbers: [10, 20, 30],
    },
    paramsSerializer: (params) => {
      return Object.keys(params)
        .map((key) => {
          return params[key].map((val) => `${key}=${val}`).join("&");
        })
        .join("&");
    },
  })
  .then((response) => console.log(response.data));
```

---

### 3. Reverse String

กลับลำดับข้อความ

```http
GET /reverse?text={text}
```

**Query Parameters:**

| Parameter | Type   | Required | Description                |
| --------- | ------ | -------- | -------------------------- |
| text      | string | Yes      | ข้อความที่ต้องการกลับลำดับ |

**Success Response 200 OK**

```json
{
  "reversed": "ebuQranoS"
}
```

**Error Response 422 Unprocessable Entity**

```json
{
  "detail": [
    {
      "loc": ["query", "text"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Examples:**

**cURL:**

```bash
# กลับลำดับข้อความ
curl "http://localhost:8000/reverse?text=SonarQube"

# กลับลำดับข้อความที่มีช่องว่าง (ต้อง encode URL)
curl "http://localhost:8000/reverse?text=Hello%20World"
```

**Python:**

```python
import requests

response = requests.get(
    "http://localhost:8000/reverse",
    params={"text": "SonarQube"}
)
print(response.json())  # {"reversed": "ebuQranoS"}

# ข้อความที่มีช่องว่าง
response = requests.get(
    "http://localhost:8000/reverse",
    params={"text": "Hello World"}
)
print(response.json())  # {"reversed": "dlroW olleH"}
```

**JavaScript:**

```javascript
// Using fetch API
fetch("http://localhost:8000/reverse?text=FastAPI")
  .then((response) => response.json())
  .then((data) => console.log(data));

// Using axios
axios
  .get("http://localhost:8000/reverse", {
    params: { text: "FastAPI" },
  })
  .then((response) => console.log(response.data));
```

## ❌ Error Handling

### HTTP Status Codes

| Status Code | Description                                               |
| ----------- | --------------------------------------------------------- |
| 200         | Success - request สำเร็จ                                  |
| 400         | Bad Request - ข้อมูลที่ส่งมาไม่ถูกต้อง                    |
| 422         | Unprocessable Entity - ข้อมูลไม่ครบหรือ format ไม่ถูกต้อง |
| 500         | Internal Server Error - เกิดข้อผิดพลาดในเซิร์ฟเวอร์       |

### Error Response Format

```json
{
  "detail": "error message here"
}
```

หรือในรูปแบบ validation errors:

```json
{
  "detail": [
    {
      "loc": ["query", "field_name"],
      "msg": "error message",
      "type": "error_type"
    }
  ]
}
```

## 💡 Best Practices

### 1. Handle Errors Properly

```python
import requests

try:
    response = requests.get(
        "http://localhost:8000/average",
        params={"numbers": [10, 20, 30]}
    )
    response.raise_for_status()  # Raise exception for 4xx/5xx status codes
    data = response.json()
    print(f"Average: {data['average']}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Response: {e.response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### 2. Use Timeouts

```python
response = requests.get(
    "http://localhost:8000/average",
    params={"numbers": [10, 20, 30]},
    timeout=5  # 5 seconds timeout
)
```

### 3. Validate Input

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All items must be numbers")

    response = requests.get(
        "http://localhost:8000/average",
        params={"numbers": numbers}
    )
    return response.json()
```

## 🧪 Testing with Different Tools

### Using HTTPie

```bash
# GET request
http GET localhost:8000/

# With query parameters
http GET localhost:8000/average numbers==10 numbers==20 numbers==30
http GET localhost:8000/reverse text=="SonarQube"
```

### Using Postman

1. สร้าง new request
2. เลือก method GET
3. ใส่ URL: `http://localhost:8000/average`
4. เพิ่ม Query Params:
   - Key: `numbers`, Value: `10`
   - Key: `numbers`, Value: `20`
   - Key: `numbers`, Value: `30`
5. กด Send

### Using Python Requests

```python
import requests

# GET request to root
response = requests.get("http://localhost:8000/")
print(response.json())

# Calculate average
response = requests.get(
    "http://localhost:8000/average",
    params={"numbers": [10, 20, 30]}
)
print(response.json())

# Reverse string
response = requests.get(
    "http://localhost:8000/reverse",
    params={"text": "Hello"}
)
print(response.json())
```

## 📊 Response Time

| Endpoint     | Average Response Time |
| ------------ | --------------------- |
| GET /        | ~10ms                 |
| GET /average | ~15ms                 |
| GET /reverse | ~12ms                 |

_Response times may vary based on server load and network conditions_

## 🔄 Rate Limiting

ยังไม่มีการใช้งาน rate limiting ในเวอร์ชันปัจจุบัน แต่สามารถเพิ่มได้โดยใช้:

- slowapi
- fastapi-limiter
- Custom middleware

## 📞 Support

หากพบปัญหาหรือมีคำถาม:

- เปิด Issue บน [GitHub](https://github.com/adithep-bm/simple-fastapi-app/issues)
- ดู [README.md](README.md) สำหรับข้อมูลเพิ่มเติม

---

**Last Updated:** January 2025
