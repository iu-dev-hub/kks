"""Ceza ve Rapor module - web pages (Team Fines-Reports)."""

from flask import Blueprint, render_template

bp = Blueprint("fines_reports", __name__, url_prefix="/fines-reports")


@bp.route("/")
def index():
    return render_template("fines_reports/index.html")
