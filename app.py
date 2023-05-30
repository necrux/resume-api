from flask import Flask

app = Flask(__name__)


@app.get("/resume")
def get_resume():
    return "Hello World! Here I am!"