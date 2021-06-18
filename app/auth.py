from flask import Blueprint, render_template, abort, session, redirect, url_for, request, flash
from jinja2 import TemplateNotFound

login = Blueprint("login", __name__, template_folder="templates")
register = Blueprint("register", __name__, template_folder="templates")


@login.route("/login", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        # Get input of fields
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        return redirect(url_for('main_page.show'))
    else:
        return render_template(f"auth/login.html")


@register.route("/register", methods=["GET", "POST"])
def show():
    try:
        return render_template(f"auth/register.html")
    except TemplateNotFound:
        abort(404)
