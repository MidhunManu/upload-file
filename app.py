from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    files = os.listdir("./uploads")
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save("./uploads/" + str(f.filename))

    return "file uploaded"

@app.route("/files/<filename>")
def files(filename):
    return send_from_directory("uploads", filename)

app.run(host="0.0.0.0", debug=True)
