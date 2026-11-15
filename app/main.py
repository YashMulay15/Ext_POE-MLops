import csv
import os
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import add

app = FastAPI(title="Addition API")

LOG_FILE = "logs/requests.csv"


class Numbers(BaseModel):
    a: float
    b: float


def log_request(a: float, b: float, result: float) -> None:
    os.makedirs("logs", exist_ok=True)
    new_file = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "a", "b", "result"])
        writer.writerow([datetime.now().isoformat(), a, b, result])


@app.get("/")
def home():
    return {"message": "Addition API is running"}


@app.post("/add")
def add_numbers(nums: Numbers):
    result = add(nums.a, nums.b)
    log_request(nums.a, nums.b, result)
    return {"a": nums.a, "b": nums.b, "result": result}