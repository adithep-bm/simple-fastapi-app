# Contributing to FastAPI Clean Code Example

ยินดีต้อนรับ! เราขอขอบคุณที่สนใจจะมีส่วนร่วมในโปรเจคนี้ 🎉

## 📋 สารบัญ

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

โปรเจคนี้ปฏิบัติตาม Code of Conduct เพื่อให้ทุกคนรู้สึกยินดีที่จะมีส่วนร่วม:

- ใช้ภาษาที่เป็นมิตรและครอบคลุมทุกคน
- เคารพมุมมองและประสบการณ์ที่แตกต่างกัน
- ยอมรับคำวิจารณ์ที่สร้างสรรค์
- มุ่งเน้นสิ่งที่ดีที่สุดสำหรับชุมชน
- แสดงความเห็นอกเห็นใจต่อสมาชิคในชุมชนคนอื่นๆ

## 🚀 Getting Started

### 1. Fork Repository

คลิกปุ่ม "Fork" ที่มุมขวาบนของหน้า repository

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/simple-fastapi-app.git
cd simple-fastapi-app
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/adithep-bm/simple-fastapi-app.git
```

### 4. Setup Development Environment

```bash
# สร้าง virtual environment
python -m venv fastapi-env

# Activate virtual environment
# Windows
.\fastapi-env\Scripts\Activate.ps1
# Linux/Mac
source fastapi-env/bin/activate

# ติดตั้ง dependencies
pip install -r requirements.txt

# ติดตั้ง development dependencies (ถ้ามี)
pip install pytest pytest-cov black flake8 mypy
```

## 💻 Development Process

### 1. Create a Branch

สร้าง branch ใหม่สำหรับการพัฒนาของคุณ:

```bash
git checkout -b feature/your-feature-name
```

ตั้งชื่อ branch ตามรูปแบบ:

- `feature/` - สำหรับ feature ใหม่
- `fix/` - สำหรับ bug fixes
- `docs/` - สำหรับการอัพเดท documentation
- `refactor/` - สำหรับการ refactor code
- `test/` - สำหรับการเพิ่ม tests

### 2. Make Your Changes

- เขียนโค้ดตาม [Coding Standards](#coding-standards)
- เพิ่ม tests สำหรับ feature ใหม่
- อัพเดท documentation ถ้าจำเป็น
- ทดสอบว่าโค้ดของคุณทำงานได้

### 3. Keep Your Branch Updated

```bash
git fetch upstream
git rebase upstream/main
```

## 📐 Coding Standards

### Python Style Guide

เราใช้ [PEP 8](https://pep8.org/) เป็น style guide หลัก

#### Formatting

ใช้ [Black](https://black.readthedocs.io/) สำหรับ auto-formatting:

```bash
black app/ tests/
```

#### Linting

ใช้ [Flake8](https://flake8.pycqa.org/) สำหรับ linting:

```bash
flake8 app/ tests/ --max-line-length=88 --extend-ignore=E203
```

#### Type Checking

ใช้ [mypy](http://mypy-lang.org/) สำหรับ static type checking:

```bash
mypy app/
```

### Code Organization

```python
# 1. Standard library imports
import os
import sys
from typing import List, Dict

# 2. Third-party imports
from fastapi import FastAPI, HTTPException
import pytest

# 3. Local imports
from app.utils import calculate_average
```

### Naming Conventions

```python
# Constants: UPPER_CASE
MAX_RETRY_COUNT = 3
API_VERSION = "1.0.0"

# Functions and variables: snake_case
def calculate_average(numbers: List[float]) -> float:
    total_sum = sum(numbers)
    return total_sum / len(numbers)

# Classes: PascalCase
class UserService:
    def __init__(self):
        pass
```

### Documentation

#### Docstrings

ใช้ Google-style docstrings:

```python
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
    """
    if not numbers:
        raise ValueError("Numbers list must not be empty")
    return sum(numbers) / len(numbers)
```

#### Comments

```python
# ดี: อธิบายว่าทำไมต้องทำแบบนี้
# ใช้ ceiling division เพราะต้องการปัดขึ้นเสมอ
result = -(-total // batch_size)

# ไม่ดี: อธิบายสิ่งที่โค้ดทำอยู่แล้ว
# เพิ่มค่า 1 ให้ x
x = x + 1
```

## 🧪 Testing Guidelines

### Writing Tests

- เขียน test สำหรับทุก feature ใหม่
- เขียน test สำหรับ bug fixes
- ตรวจสอบ edge cases
- รักษา code coverage ไว้ที่อย่างน้อย 80%

#### Test Structure

```python
def test_function_name_should_expected_behavior():
    """
    ชื่อ test ควรบอกว่าทดสอบอะไรและคาดหวังผลลัพธ์อะไร
    """
    # Arrange: เตรียมข้อมูล
    numbers = [10, 20, 30]

    # Act: เรียกใช้ฟังก์ชัน
    result = calculate_average(numbers)

    # Assert: ตรวจสอบผลลัพธ์
    assert result == 20.0
```

#### Test Examples

```python
# ✅ ดี: ชื่อ test ชัดเจน
def test_calculate_average_with_positive_numbers_returns_correct_average():
    assert calculate_average([10, 20, 30]) == 20.0

def test_calculate_average_with_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average([])

# ❌ ไม่ดี: ชื่อ test ไม่ชัดเจน
def test_average():
    assert calculate_average([10, 20, 30]) == 20.0

def test_error():
    with pytest.raises(ValueError):
        calculate_average([])
```

### Running Tests

```bash
# รัน tests ทั้งหมด
pytest

# รัน tests พร้อม coverage
pytest --cov=app --cov-report=html

# รัน tests specific file
pytest tests/test_main.py

# รัน tests specific function
pytest tests/test_main.py::test_root
```

### Coverage Requirements

- Code coverage ควรอยู่ที่อย่างน้อย **80%**
- Feature ใหม่ควรมี coverage **90%** ขึ้นไป

ตรวจสอบ coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

## 📝 Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: Feature ใหม่
- `fix`: Bug fix
- `docs`: การเปลี่ยนแปลง documentation
- `style`: การเปลี่ยนแปลงที่ไม่กระทบโค้ด (formatting, white-space)
- `refactor`: Code refactoring
- `test`: เพิ่มหรือแก้ไข tests
- `chore`: งานอื่นๆ (update dependencies, build tasks)

### Examples

```bash
# Feature
git commit -m "feat(api): add endpoint for user statistics"

# Bug fix
git commit -m "fix(utils): correct average calculation for empty list"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Refactor
git commit -m "refactor(main): simplify error handling logic"

# Test
git commit -m "test(utils): add edge case tests for reverse_string"
```

### Detailed Example

```
feat(api): add pagination support for user list endpoint

- Add page and limit query parameters
- Update response format to include metadata
- Add tests for pagination logic

Closes #123
```

## 🔄 Pull Request Process

### Before Submitting

1. ตรวจสอบว่าโค้ดทำงานได้ถูกต้อง
2. รัน tests และตรวจสอบว่าผ่านหมด
3. ตรวจสอบ code coverage
4. Format โค้ดด้วย Black
5. ตรวจสอบด้วย Flake8
6. อัพเดท documentation ถ้าจำเป็น

### Checklist

```bash
# รัน tests
pytest --cov=app

# Format code
black app/ tests/

# Lint code
flake8 app/ tests/ --max-line-length=88

# Type check
mypy app/
```

### Creating Pull Request

1. Push branch ของคุณไปยัง fork:

```bash
git push origin feature/your-feature-name
```

2. ไปที่ GitHub repository และคลิก "New Pull Request"

3. เลือก base repository และ branch:

   - Base repository: `adithep-bm/simple-fastapi-app`
   - Base branch: `main`
   - Head repository: `YOUR-USERNAME/simple-fastapi-app`
   - Compare branch: `feature/your-feature-name`

4. กรอกข้อมูล PR:

```markdown
## Description

อธิบายว่าเปลี่ยนแปลงอะไรและทำไม

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

อธิบายว่าทดสอบอย่างไร

## Checklist

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Added tests for new features
- [ ] Updated documentation
- [ ] No breaking changes (or documented)
```

### Review Process

1. รอ maintainers review PR ของคุณ
2. ตอบคำถามหรือแก้ไขตาม feedback
3. เมื่อได้รับ approval, PR จะถูก merge

## 🐛 Reporting Bugs

### Before Reporting

- ตรวจสอบว่ามี issue ที่คล้ายกันอยู่แล้วหรือไม่
- ตรวจสอบว่าใช้เวอร์ชันล่าสุดหรือไม่

### Bug Report Template

```markdown
## Description

อธิบาย bug ที่พบ

## To Reproduce

Steps to reproduce:

1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior

อธิบายว่าควรทำงานอย่างไร

## Actual Behavior

อธิบายว่าทำงานอย่างไรจริงๆ

## Environment

- OS: [e.g., Windows 11]
- Python version: [e.g., 3.11]
- FastAPI version: [e.g., 0.111.0]

## Additional Context

เพิ่มข้อมูลอื่นๆ เช่น screenshots, logs
```

## 💡 Feature Requests

### Feature Request Template

```markdown
## Feature Description

อธิบาย feature ที่ต้องการ

## Problem Statement

อธิบายปัญหาที่ feature นี้จะช่วยแก้

## Proposed Solution

อธิบายว่าควรทำงานอย่างไร

## Alternatives Considered

มีทางเลือกอื่นๆ ที่พิจารณาแล้วหรือไม่

## Additional Context

เพิ่มข้อมูลอื่นๆ
```

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## 🙏 Thank You!

ขอบคุณที่มีส่วนร่วมในโปรเจคนี้! การมีส่วนร่วมทุกอย่างมีค่ามาก ไม่ว่าจะเป็น bug reports, feature requests, documentation improvements, หรือ code contributions.

---

หากมีคำถาม กรุณาเปิด issue หรือติดต่อ maintainers ได้เลย!
