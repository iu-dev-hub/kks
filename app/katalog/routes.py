"""Katalog modülünün web sayfaları (Ekip 2)."""

from flask import Blueprint, render_template

bp = Blueprint("katalog", __name__, url_prefix="/katalog")


@bp.route("/")
def index():
    return render_template("katalog/index.html")
