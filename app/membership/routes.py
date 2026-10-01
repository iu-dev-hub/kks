"""Üyelik module - web pages (Team Membership)."""

from flask import Blueprint, render_template

bp = Blueprint("membership", __name__, url_prefix="/membership")


@bp.route("/")
def index():
    return render_template("membership/index.html")
