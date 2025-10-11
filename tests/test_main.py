# tests/test_main.py
"""
Unit tests สำหรับ FastAPI application endpoints

Test suite นี้ครอบคลุมการทดสอบทุก endpoint และ edge cases
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """ทดสอบ root endpoint ว่าส่งข้อความต้อนรับที่ถูกต้อง"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from FastAPI with Jenkins & SonarQube!"
    }


def test_average_success():
    """ทดสอบการคำนวณค่าเฉลี่ยที่สำเร็จ"""
    response = client.get("/average?numbers=10&numbers=20&numbers=30")
    assert response.status_code == 200
    assert response.json()["average"] == 20.0


def test_average_empty_list():
    """ทดสอบการส่ง request โดยไม่มี query parameter"""
    response = client.get("/average")
    assert response.status_code == 422  # missing query parameter


def test_reverse_string():
    """ทดสอบการกลับลำดับข้อความ"""
    response = client.get("/reverse?text=SonarQube")
    assert response.status_code == 200
    assert response.json()["reversed"] == "ebuQranoS"
