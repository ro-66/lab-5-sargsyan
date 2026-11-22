from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "Robert", "age": 21},
    {"id": 2, "name": "Alex", "age": 22}
]

@app.get("/")
def home():
    return {"message": "DevOps Lab 5"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}
