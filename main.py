from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.secret_key = 'UOAFNONFUA9128381.+RJN1'

if __name__ == "__main__":
    app.run()
