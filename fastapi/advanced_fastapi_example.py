from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
import sqlite3

app = FastAPI()

# Define API key security scheme
api_key = APIKeyHeader(name="API-Key")

# Define custom user authentication middleware
async def authenticate_user(api_key: str = Depends(api_key)):
    if api_key != "your_api_key":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
async def read_root():
    return {"message": "Hello, this is a FastAPI server!"}

# Mocking user data for demonstration
user_db = {
    "user_id": {
        "name": "John Doe",
        "email": "johndoe@example.com",
    }
}

@app.get("/user/{user_id}")
async def read_user(user_id: str, auth=Depends(authenticate_user)):
    user = user_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create and connect to SQLite database
conn = sqlite3.connect('your_database.db')

@app.get("/get_data")
async def get_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    return {"data": data}
