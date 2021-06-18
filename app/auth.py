from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

login = Blueprint("login", __name__, template_folder="templates")
register = Blueprint("register", __name__, template_folder="templates")


@login.route("/login")
def show():
    try:
        return render_template(f"auth/login.html")
    except TemplateNotFound:
        abort(404)


@register.route("/register")
def show():
    try:
        return render_template(f"auth/register.html")
    except TemplateNotFound:
        abort(404)
