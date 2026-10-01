"""Katalog module - web pages (Team Catalog)."""

from flask import Blueprint, render_template

bp = Blueprint("catalog", __name__, url_prefix="/catalog")


@bp.route("/")
def index():
    return render_template("catalog/index.html")
