# stats_service.py
from fastapi import FastAPI
import random
import uuid

app = FastAPI()

post_stats = {}


@app.post("/post-stats/{post_id}", response_model=dict)
def add_post_stats(post_id: str):
    if post_id not in post_stats:
        post_stats[post_id] = {
            "total_likes": random.randint(1, 100),
            "total_dislikes": random.randint(1, 50)
        }
    return post_stats[post_id]
