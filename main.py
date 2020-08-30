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

@app.route("/privacy_policy")
def privacy_policy_redirect():
    return redirect("/privacy_policy/", code=302)
@app.route("/privacy_policy/")
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route("/recipes")
def all_recipes_redirect():
    return redirect("/recipes/", code=302)
@app.route("/recipes/")
def all_recipes():
    return render_template("all_recipes.html")

@app.route("/recipes/cookie_dough_cupcakes")
def cookie_dough_cupcakes_redirect():
    return redirect("/recipes/cookie_dough_cupcakes/", code=302)
@app.route("/recipes/cookie_dough_cupcakes/")
def cookie_dough_cupcakes():
    return render_template("recipes/cookie_dough_cupcakes.html")

@app.route("/recipes/lemon_chicken")
def lemon_chicken_redirect():
    return redirect("/recipes/lemon_chicken/", code=302)
@app.route("/recipes/lemon_chicken/")
def lemon_chicken():
    return render_template("recipes/lemon_chicken.html")

@app.route("/recipes/sweet_cream_cold_brew")
def sweet_cream_cold_brew_redirect():
    return redirect("/recipes/sweet_cream_cold_brew/", code=302)
@app.route("/recipes/sweet_cream_cold_brew/")
def sweet_cream_cold_brew():
    return render_template("recipes/sweet_cream_cold_brew.html")

@app.route("/experiments")
def experiments_redirect():
    return redirect("/experiments/", code=302)
@app.route("/experiments/")
def experiments():
    return render_template("experiments.html")

@app.route("/experiments/edible_cookie_dough")
def edible_cookie_dough_redirect():
    return redirect("/experiments/edible_cookie_dough/", code=302)
@app.route("/experiments/edible_cookie_dough/")
def edible_cookie_dough():
    return render_template("experiments/edible_cookie_dough.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

secret_path = path.join(app.root_path, 'secret_key')
if path.exists(secret_path):
    app.secret_key = bytes(open(secret_path, 'r').read().rstrip(), 'UTF-8')
else:
    # For development only:
    app.secret_key = b'AYfNiTbyX5gH0ILcdrjGRA'

if __name__ == "__main__":
    app.run()
