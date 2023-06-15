from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route to homepage
    :return: index.html
    """
    return render_template('index.html')


@app.route('/play')
def play():
    """
    Route to play game page
    :return: play.html
    """

    return render_template('play.html')


if __name__ == "__main__":
    app.run()
