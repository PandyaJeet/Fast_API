from fastapi import FastAPI, HTTPException
from src.fastapi_test.schemas import PostCreate
app = FastAPI()

text_post = {
    1: {
        "title": "My first post",
        "content": "This is my first post content"
    },
    2: {
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern Python framework for building APIs."
    },
    3: {
        "title": "Python Programming",
        "content": "Python is a powerful and beginner-friendly programming language."
    },
    4: {
        "title": "Understanding APIs",
        "content": "APIs allow different software applications to communicate with each other."
    },
    5: {
        "title": "My Coding Journey",
        "content": "I am learning backend development and building projects with Python."
    },
    6: {
        "title": "REST API Basics",
        "content": "REST APIs use HTTP methods such as GET, POST, PUT, and DELETE."
    },
    7: {
        "title": "Backend Development",
        "content": "Backend development handles business logic, databases, authentication, and APIs."
    },
    8: {
        "title": "Learning Git",
        "content": "Git helps developers track changes and collaborate on software projects."
    },
    9: {
        "title": "Database Concepts",
        "content": "Databases are used to store, organize, and retrieve application data."
    },
    10: {
        "title": "Building Projects",
        "content": "Building practical projects is one of the best ways to improve programming skills."
    },
    11: {
        "title": "Next Steps",
        "content": "My next goal is to build a complete backend application using FastAPI."
    }
}

@app.get("/posts")
def get_posts(limit: int = None): ##Query Parameter: funcs that are not a part of the path parameter are considered query parameters.
    if limit:##The query is a set of key-value pairs that are sent in the URL after the question mark (?). For example, in the URL /posts?limit=5, limit is a query parameter with a value of 5.
        return list(text_post.values())[:limit]
    return text_post

@app.get("/posts/{post_id}")##Path Parameter: The value for post_id will be passed to your function as the args for post_id.
def get_post(post_id: int):##Declares post_id is int type, FastAPI will automatically validate the input and return a 422 error if the value is not an integer
    if post_id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_post.get(post_id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_post[max(text_post.keys()) + 1] = {"title": post.title, "content": post.content}
    return new_post

@app.delete("/posts")
def delete_post():
    last_post = max(text_post.keys())
    delete_post = text_post.pop(last_post)
    return delete_post