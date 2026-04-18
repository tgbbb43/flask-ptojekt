from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from errors import *
from routes import tasks_bp
from errors import error_bp

app = Flask(__name__)
    


app.register_blueprint(tasks_bp)
app.register_blueprint(error_bp)

   

if __name__ == "__main__":
    app.run(debug=True)