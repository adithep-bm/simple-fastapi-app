# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)


@app.get("/")
def root():
    """
    Root endpoint สำหรับตรวจสอบสถานะของ API

    Returns:
        dict: ข้อความต้อนรับ
    """
    return {"message": "Hello from FastAPI with Jenkins & SonarQube!"}


@app.get("/average")
def get_average(numbers: List[float] = Query(..., description="List ของตัวเลข")):
    """
    คำนวณค่าเฉลี่ยจาก list ของตัวเลข

    Args:
        numbers: รายการตัวเลขที่ต้องการคำนวณค่าเฉลี่ย (สามารถส่งหลายค่าได้)

    Returns:
        dict: ผลลัพธ์ค่าเฉลี่ย

    Raises:
        HTTPException: หากรายการตัวเลขว่างเปล่า (status_code=400)

    Example:
        GET /average?numbers=10&numbers=20&numbers=30
        Response: {"average": 20.0}
    """
    try:
        result = calculate_average(numbers)
        return {"average": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/reverse")
def get_reverse(text: str = Query(..., description="ข้อความที่ต้องการกลับ")):
    """
    กลับลำดับข้อความ (reverse string)

    Args:
        text: ข้อความที่ต้องการกลับลำดับ

    Returns:
        dict: ข้อความที่ถูกกลับลำดับแล้ว

    Example:
        GET /reverse?text=SonarQube
        Response: {"reversed": "ebuQranoS"}
    """
    result = reverse_string(text)
    return {"reversed": result}
