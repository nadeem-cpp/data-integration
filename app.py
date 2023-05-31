from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("files")
    try:
        for file in files:
            file.save(dst=f"uploaded/{file.filename}")
        return "uploaded"
    except Exception as e:
        return redirect(url_for("home"), code=302,)


if __name__ == '__main__':
    app.run(debug=True)
