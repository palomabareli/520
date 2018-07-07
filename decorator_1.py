#!/usr/bin/python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("<h1>Hello Word!!!</h1>")

if __name__ == "__main__"   
    app.run(host="0.0.0.0", port=5000, debug=True)