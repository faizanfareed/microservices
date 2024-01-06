# users_service.py
from fastapi import FastAPI
import random

app = FastAPI()

active_users = {}


@app.post("/total-active-users", response_model=dict)
def add_total_active_users():
    total_active_users = {"total_active_users": random.randint(50, 1000)}
    active_users.update(total_active_users)
    return total_active_users
