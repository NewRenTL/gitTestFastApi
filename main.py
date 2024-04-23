from fastapi import FastAPI

from fastapi.responses import FileResponse

from random import randint

import os

from fastapi import FastAPI,File,UploadFile

import uuid

app = FastAPI()

IMAGEDIR = "images/"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload/")
async def create_upload_file(file:UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    #save the file 

    with open(f"{IMAGEDIR}{file.filename}","wb") as f:
        f.write(contents)

    return {"filename":file.filename}

@app.get("/show/")
async def read_random_file():
    files = os.listdir(IMAGEDIR)
    random_index = randint(0,len(files)-1)

    path=f"{IMAGEDIR}{files[random_index]}"

    return FileResponse(path)