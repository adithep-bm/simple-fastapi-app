# app/utils.py
"""
Utility functions สำหรับการคำนวณและจัดการข้อมูล

Module นี้ประกอบด้วย helper functions ที่ใช้ในการประมวลผลข้อมูล
"""
from typing import List


def calculate_average(numbers: List[float]) -> float:
    """
    คำนวณค่าเฉลี่ยจาก list ของตัวเลข

    Args:
        numbers: รายการตัวเลขที่ต้องการคำนวณค่าเฉลี่ย

    Returns:
        float: ค่าเฉลี่ยของตัวเลขทั้งหมด

    Raises:
        ValueError: หากรายการตัวเลขว่างเปล่า

    Example:
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([1.5, 2.5, 3.0])
        2.333...
    """
    if not numbers:
        raise ValueError("Numbers list must not be empty")
    return sum(numbers) / len(numbers)


def reverse_string(text: str) -> str:
    """
    กลับลำดับข้อความ

    Args:
        text: ข้อความที่ต้องการกลับลำดับ

    Returns:
        str: ข้อความที่ถูกกลับลำดับแล้ว

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("FastAPI")
        'IPAtsaF'
    """
    return text[::-1]
