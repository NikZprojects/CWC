from flask import Flask, session, redirect, url_for, escape, request, render_template
from os import path, environ

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_redirect():
    return redirect("/about/", code=302)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/recipes")
def all_recipes_redirect():
    return redirect("/recipes/", code=302)

@app.route("/recipes/")
def all_recipes():
    return render_template("all_recipes.html")

@app.route("/experiments")
def experiments_redirect():
    return redirect("/experiments/", code=302)

@app.route("/experiments/")
def experiments():
    return render_template("experiments.html")

@app.route("/privacy_policy")
def privacy_policy_redirect():
    return redirect("/privacy_policy/", code=302)

@app.route("/privacy_policy/")
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route("/recipes/espresso")
def espresso_redirect():
    return redirect("/recipes/espresso/", code=302)

@app.route("/recipes/espresso/")
def espresso():
    return render_template("recipes/espresso.html")

@app.route("/recipes/cold_brew")
def cold_brew_redirect():
    return redirect("/recipes/cold_brew/", code=302)

@app.route("/recipes/cold_brew/")
def cold_brew():
    return render_template("recipes/cold_brew.html")

@app.route("/recipes/cookie_dough_cupcakes")
def cookie_dough_cupcakes_redirect():
    return redirect("/recipes/cookie_dough_cupcakes/", code=302)

@app.route("/recipes/cookie_dough_cupcakes/")
def cookie_dough_cupcakes():
    return render_template("recipes/cookie_dough_cupcakes.html")

@app.route("/experiments/edible_cookie_dough")
def edible_cookie_dough_redirect():
    return redirect("/experiments/edible_cookie_dough/", code=302)

@app.route("/experiments/edible_cookie_dough/")
def edible_cookie_dough():
    return render_template("experiments/edible_cookie_dough.html")

secret_path = path.join(app.root_path, 'secret_key')
if path.exists(secret_path):
    app.secret_key = bytes(open(secret_path, 'r').read().rstrip(), 'UTF-8')
else:
    # For development only:
    app.secret_key = b'AYfNiTbyX5gH0ILcdrjGRA'

if __name__ == "__main__":
    app.run()
