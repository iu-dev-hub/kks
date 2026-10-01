"""Kampüs Kütüphane Sistemi (KKS) uygulama fabrikası.

Her modül bir Flask Blueprint'tir ve ayrı bir ekibe aittir:
    app/uyelik/     -> Ekip 1
    app/katalog/    -> Ekip 2
    app/odunc/      -> Ekip 3
    app/ceza_rapor/ -> Ekip 4
    app/ortak/      -> Tüm ekipler (değişiklikler Scrum of Scrums'ta konuşulur)
"""

import os

from flask import Flask, jsonify, render_template

from app.ortak import db


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("KKS_SECRET_KEY", "gelistirme-anahtari"),
        DATABASE=os.path.join(app.instance_path, "kks.sqlite"),
    )
    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    from app.ceza_rapor import bp as ceza_rapor_bp
    from app.katalog import bp as katalog_bp
    from app.odunc import bp as odunc_bp
    from app.uyelik import bp as uyelik_bp

    app.register_blueprint(uyelik_bp)
    app.register_blueprint(katalog_bp)
    app.register_blueprint(odunc_bp)
    app.register_blueprint(ceza_rapor_bp)

    @app.route("/")
    def anasayfa():
        return render_template("anasayfa.html")

    @app.route("/saglik")
    def saglik():
        """Sistemin ayakta olup olmadığını gösterir (duman testi için)."""
        return jsonify(durum="ok", surum="0.1.0")

    return app
