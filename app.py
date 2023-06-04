from flask import Flask, render_template, redirect, request, url_for
from model import DataHandler
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():
    # TODO 1 get files from form and send it to Data Handler object
    files = request.files.getlist("files")
    try:

        dh = DataHandler(data_files=files)
        titles = dh.get_similar_titles()
        return render_template("matching.html", titles=titles)

    except Exception as e:
        print(e)
        return redirect(url_for("home"), code=302,)


data = [('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games'),
        ('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games'),
        ('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games')]


@app.route("/matching")
def matching():
    return render_template("matching.html", titles=data, enumerate=enumerate)


if __name__ == '__main__':
    app.run()
