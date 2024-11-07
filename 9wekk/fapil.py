from fastapi import FastAPI, Form
import os
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id" : item_id, "name":name,"age":age}

@app.post("/plus")
async def plus_form(num1: int= Form(...), num2:int=Form(...), num3: int= Form(...), num4:int=Form(...)):
    result = num1 + num2
    result2 = num3 + num4
    return {"msg": f"{num1}+{num2}={result} | {num3}+{num4}={result2}"}

@app.post("/user")
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    return{"msg":f"{major} {name}님 ({studentcode}) 반갑습니다"}

from fastapi import File, UploadFile
import shutil
from pathlib import Path

@app.post("/uploadfile/")
async def create__upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return{"filename": file.filename, "location": str(save_path)}

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="./static", html=True), name="static")
# static_directory = os.path.abspath("c:/Users/codns/Desktop/대학교/202110481/9week/static")
# app.mount("/", StaticFiles(directory=static_directory, html=True), name="static")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")

