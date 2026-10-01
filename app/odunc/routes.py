"""Ödünç modülünün web sayfaları (Ekip 3)."""

from flask import Blueprint, render_template

bp = Blueprint("odunc", __name__, url_prefix="/odunc")


@bp.route("/")
def index():
    return render_template("odunc/index.html")
