# comments_service.py
import uuid
import random
from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker

app = FastAPI()
fake = Faker()


class Comment(BaseModel):
    text: str
    user: str


@app.post("/post-comments/{post_id}", response_model=list)
async def add_post_comment(post_id: str):
    auto_comments = []

    for _ in range(1, random.randint(1, 7)):
        comment_id = str(uuid.uuid4())
        fake_text = fake.sentence()
        fake_user = fake.user_name()
        auto_comment_data = {"id": comment_id, "text": fake_text, "user": fake_user}
        auto_comments.append(auto_comment_data)

    return auto_comments
