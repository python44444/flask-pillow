from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["unko"]
    img = Image.open(file)
    frame = Image.open("static/images/frame.png")

    resized_frame = frame.resize((img.width, img.height))
    img.paste(resized_frame, (0, 0), resized_frame)

    img.save("static/images/out.png")
    unko2 = "static/images/out.png"
    return render_template("upload.html", unko3=unko2)


if __name__ == "__main__":
    app.run(debug=True)
