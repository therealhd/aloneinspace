from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route to homepage
    :return: index.html
    """
    return render_template('index.html')


@app.route('/game')
def game():
    """
    Route to play game page
    :return: game.html
    """

    return render_template('game.html')


if __name__ == "__main__":
    app.run()
