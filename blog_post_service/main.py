# blog_post_service.py
from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import httpx
import os
from faker import Faker

app = FastAPI()
fake = Faker()


class BlogPost(BaseModel):
    title: str
    content: str


POST_STATS_SERVICE_URL = os.environ.get("POST_STATS_SERVICE_URL", "http://0.0.0.0:8003/post-stats")
POST_COMMENTS_SERVICE_URL = os.environ.get("POST_COMMENTS_SERVICE_URL", "http://0.0.0.0:8002/post-comments")


@app.get("/blog-post", response_model=dict)
async def create_blog_post():
    post_id = str(uuid.uuid4())

    # Generate fake data using Faker
    fake_title = fake.sentence()
    fake_content = fake.paragraph()

    post_data = {"id": post_id, "title": fake_title, "content": fake_content}

    # Generate dummy stats data
    stats_data = {}

    # Call the Post Stats service with dummy data
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{POST_STATS_SERVICE_URL}/{post_id}", json=stats_data)
            stats_data = response.json()
        response.raise_for_status()
    except httpx.HTTPError as exc:
        # Handle error calling Post Stats service
        print('EXCEP', exc)
        # return {"error": f"Error calling Post Stats service: {exc}"}
        pass

    comments_data = {}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{POST_COMMENTS_SERVICE_URL}/{post_id}", json=comments_data)
            comments_data = response.json()
        response.raise_for_status()
    except httpx.HTTPError as exc:
        # Handle error calling Post Stats service
        print('Exception in comments_data : ', exc)
        # return {"error": f"Error calling Post Stats service: {exc}"}
        pass

    return {"post": post_data, "stats": stats_data, "comments": comments_data}
