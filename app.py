from flask import Flask, render_template, redirect, request, url_for
from model import DataHandler
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    # TODO 1 get files from form and send it to Data Handler object
    files = request.files.getlist("files")
    sep = request.form["sep"]
    try:

        dh = DataHandler(data_files=files)
        matched_columns = dh.get_similar_titles()
        print(matched_columns)
        return render_template("matching.html", titles=matched_columns)

    except Exception as e:
        print(e)
        return redirect(url_for("home"), code=302,)


data = [('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games'),
        ('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games'),
        ('fruit', 'country'), ('brand', 'drink'), ('pet', 'Has Car'), ('Likes Pizza', 'Plays Games')]


@app.route("/matching")
def matching():
    return render_template("matching.html", titles=data, enumerate=enumerate)


@app.route("/contactus")
def contact_us():
    return render_template("contact.html")


@app.route("/email", methods=["POST", "GET"])
def email():
    name = request.form["name"]
    email = request.form["email"]
    # send email from above email to system
    return "<h1>Message submitted</h1>"


if __name__ == '__main__':
    app.run()
