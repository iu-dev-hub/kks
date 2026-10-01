"""Üyelik modülünün web sayfaları (Ekip 1)."""

from flask import Blueprint, render_template

bp = Blueprint("uyelik", __name__, url_prefix="/uyelik")


@bp.route("/")
def index():
    return render_template("uyelik/index.html")
