"""Ceza ve Rapor modülünün web sayfaları (Ekip 4)."""

from flask import Blueprint, render_template

bp = Blueprint("ceza_rapor", __name__, url_prefix="/ceza-rapor")


@bp.route("/")
def index():
    return render_template("ceza_rapor/index.html")
