from flask import (
  Flask,
  request
  )
from app.database import task

app = Flask(__name__)

# REST - Represnetational State Transfer - Architectural Design Pattern for
# building network connected services


@app.get("/")            
@app.get("/tasks")
def scan():
  out = {
    "tasks": task.scan(),
    "ok": True
  }
  return out                            #by default, Flask wuill return as tatus code of 200                              

@app.put("/tasks/<int:pk>/")
def update(pk):
  task_data = request.json
  task.update_by_id(task_data, pk)
  return "", 204                        #204 is no content (sucessful, but there's nothing to return)

@app.post("/tasks/")
def add():
  task_data = request.json
  task.insert(task_data)
  return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_by_id(pk):
  task.delete_by_id( pk)
  return "", 204

@app.get("/tasks/<int:pk>/")
def select_by_id(pk):
  single_task = task.select_by_id(pk)
  out = {
    "task": task.select_by_id,
    "ok": True
  }
  if not single_task:
    out["ok"] = False
    out["message"] = "Task not found"
    return out, 404
  out["task"] = single_task
  return out




