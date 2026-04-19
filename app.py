from flask import Flask, render_template
from db import init_db
from routes.tasks import tasks_bp

app = Flask(__name__)


init_db(app)


app.register_blueprint(tasks_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)