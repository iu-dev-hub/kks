"""Kampüs Kütüphane Sistemi (KKS) - application factory.

Her modül bir Flask Blueprint'tir ve ayrı bir ekibe aittir:
    app/membership/     -> Team Membership    (Üyelik)
    app/catalog/        -> Team Catalog       (Katalog)
    app/loans/          -> Team Loans         (Ödünç)
    app/fines_reports/  -> Team Fines-Reports (Ceza ve Rapor)
    app/core/           -> Tüm ekipler (değişiklikler Scrum of Scrums'ta konuşulur)
"""

import os

from flask import Flask, jsonify, render_template

from app.core import db

VERSION = "0.1.0"


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("KKS_SECRET_KEY", "dev-secret-key"),
        DATABASE=os.path.join(app.instance_path, "kks.sqlite"),
    )
    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    from app.catalog import bp as catalog_bp
    from app.fines_reports import bp as fines_reports_bp
    from app.loans import bp as loans_bp
    from app.membership import bp as membership_bp

    app.register_blueprint(membership_bp)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(loans_bp)
    app.register_blueprint(fines_reports_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/health")
    def health():
        """Sistemin ayakta olup olmadığını gösterir (smoke test için)."""
        return jsonify(status="ok", version=VERSION)

    return app
