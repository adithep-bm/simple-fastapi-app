import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"message": "HELLO, FASTAPI!"}
