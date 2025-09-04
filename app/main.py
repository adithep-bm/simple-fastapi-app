
from fastapi import FastAPI
from .utils import to_uppercase

app = FastAPI()

@app.get("/")
def read_root():
	message = to_uppercase("Hello, FastAPI!")
	return {"message": message}
