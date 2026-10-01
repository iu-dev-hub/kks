"""Ödünç module - web pages (Team Loans)."""

from flask import Blueprint, render_template

bp = Blueprint("loans", __name__, url_prefix="/loans")


@bp.route("/")
def index():
    return render_template("loans/index.html")
