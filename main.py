from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route("/")
def task():
    return jsonify({
        "message": "API Is Running"
    })
    
tasks = [{
    "id": 1,
    "title": "Learn Flask",
    "completed": False
},
{ 
    "id": 2,
    "title": "Build API",
    "completed": False
}, 
{ 
    "id": 3,
    "title": "Test with Postman",
    "completed": True
} ] 

task_id_counter = 4   

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/task/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    for t in tasks:
        if t["id"] == task_id:
            return jsonify({
                "task" : t
            }),200
    return jsonify({
        "error" : "not found"
    }),404
    

@app.route("/tasks", methods=['POST'])
def add_task():
    global task_id_counter  
    request_data = request.get_json()
    new_task = {
        "id": task_id_counter,       
        "title": request_data.get("title"),
        "completed": request_data.get("completed", False) 
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=['PUT']) 
def update_task(task_id):
    request_data = request.get_json()
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = request_data.get("title", t["title"])
            t["completed"] = request_data.get("completed", t["completed"])
            
            return jsonify({
                "message": "Task updated successfully",
                "task": t
            }), 200
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=['DELETE']) 
def delete_task(task_id): 
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t) 
            return jsonify({
                "message": "Task deleted successfully",
                "deleted_task": t
            }), 200
    return jsonify({"error": "Task not found"}), 404
    
    

if __name__ == "__main__":
    app.run(debug=True)