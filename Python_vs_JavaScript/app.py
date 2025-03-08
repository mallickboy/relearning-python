from fastapi import FastAPI, UploadFile

app= FastAPI()

@app.get("/")
def home():
    return {"data": "Welcome to Home Page."}

@app.get("/contact")
def contact():
    return {"data": "Welcome to Contact Page."}

@app.post("/upload")
def handle_image(files:list[UploadFile]):
    print(files)
    return {"status": "got the files"}

import uvicorn
uvicorn.run(app)