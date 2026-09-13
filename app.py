from flask import Flask, request, jsonify
from flask_cors import CORS

from ai_generator import generate_website

import os


app = Flask(__name__)

CORS(app)


UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return "AI Screenshot-to-Website Generator is running"


@app.route(
    "/generate",
    methods=["POST"]
)
def generate():

    if "screenshot" not in request.files:

        return jsonify({
            "error":
            "Screenshot not found"
        }), 400


    screenshot =
        request.files["screenshot"]


    file_path = os.path.join(
        UPLOAD_FOLDER,
        screenshot.filename
    )


    screenshot.save(file_path)


    result =
        generate_website(file_path)


    return jsonify(result)


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )