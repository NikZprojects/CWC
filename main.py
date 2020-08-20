from flask import Flask, session, redirect, url_for, escape, request, render_template

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

@app.route("/recipes/avocado_toast")
def avocado_toast_redirect():
    return redirect("/recipes/avocado_toast/", code=302)

@app.route("/recipes/avocado_toast/")
def avocado_toast():
    return render_template("recipes/avocado_toast.html")

app.secret_key = 'UOAFNONFUA9128381.+RJN1'

if __name__ == "__main__":
    app.run()
