from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_page = Blueprint('main_page', __name__, template_folder='templates')


@main_page.route('/')
def show():
    try:
        return render_template(f"main_page/main_page.html")
    except TemplateNotFound:
        return abort(404)
