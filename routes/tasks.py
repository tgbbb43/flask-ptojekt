from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from models import tasks
from db import get_collection
import uuid
tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    col = get_collection("todo")
    all_tasks = list(col.find())
    for task in all_tasks:
        task["_id"] = str(task["_id"])
    return jsonify(all_tasks)




@tasks_bp.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id: str):
    col = get_collection("todo")
    task = col.find_one({"_id":task_id})
    if not task:
        raise NotFound(f"Task {task_id} not found")
    task["_id"] = str(task["_id"])  
    return jsonify(task)


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    col = get_collection("todo")
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        raise BadRequest("request body must be json")
    if "title" not in data:
        raise BadRequest("title is required")
    title = data["title"]
    if not isinstance(title, str):
        raise BadRequest("title must be a string")
    if not title.strip():
        raise UnprocessableEntity("title must contain text")

    # New tasks get a generated id and start as incomplete.
    new_task = {
        "_id": str(uuid.uuid4()),
        "title": title.strip(),
        "completed": False  
    }
    
    col.insert_one(new_task)

    
    new_task["_id"] = str(new_task["_id"])
    return jsonify({
        "success": True,
        "data": new_task
    }), 201




@tasks_bp.route("/tasks/<task_id>", methods=["PUT"])
def change_task(task_id):
    data = request.get_json(silent=True)
    col = get_collection("todo")
    if not data or not isinstance(data, dict):
        raise BadRequest("error: update request must contain data")

    
    allowed_keys = ("title", "completed")
    for key in data:
        if key not in allowed_keys:
            raise BadRequest(f"not allowed to pass {key}")

    
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            raise BadRequest("title must be a non-empty string")
        data["title"] = data["title"].strip() 

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            raise BadRequest("completed must be a boolean")

 
    result =col.update_one(
        {"_id": str(task_id)},
        {"$set": data} 
    )

  
    if result.matched_count == 0:
        raise NotFound(f"{task_id} not found")

    return jsonify({"success": True, "updated_fields": data})
@tasks_bp.route("/tasks/<task_id>", methods=["PATCH"])
def patch_task_completed(task_id):
    data = request.get_json()
    col = get_collection("todo")
   
    result = col.update_one(
        {"_id": str(task_id)},
        {"$set": {"completed": data.get("completed")}}
    )
    
  
    if result.matched_count == 0:
        raise NotFound(f"task {task_id} not found")
            
    return {"message": "updated successfully"}

@tasks_bp.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    col = get_collection("todo")
    result = col.delete_one({"_id":task_id})

    if result.deleted_count == 0:
        raise NotFound(f"{task_id} not found")

    return {"Message": "task removed successfully"}