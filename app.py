from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route to homepage
    :return: index.html
    """
    return 'index.html'


if __name__ == "__main__":
    app.run()