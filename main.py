from fastapi import FastAPI,HTTPException
import json
app =FastAPI()
@app.get("/")
def root():
    return{
        "message":"its runing"
    }
@app.get("/mathely")
def root1():
    return {"message": "hello"}
@app.get("/student/{student_id}")
def root2(student_id : int):
    with open("data.json","r") as file:
        data=json.load(file)
    for s in data["students"]:
        if s["id"]==student_id:
            return s 
    raise HTTPException (status_code=404,detail="mathely pagal hai")
