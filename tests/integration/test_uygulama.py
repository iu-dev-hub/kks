"""ÖRNEK entegrasyon testleri: Flask test istemcisi ile.

Tarayıcı açmadan HTTP istekleri gönderir; birim testlerden yavaş,
E2E testlerden çok daha hızlıdır.
"""

import pytest

from app.ortak.db import get_db


def test_saglik_kontrolu(client):
    yanit = client.get("/saglik")
    assert yanit.status_code == 200
    assert yanit.get_json()["durum"] == "ok"


def test_anasayfa_acilir(client):
    yanit = client.get("/")
    assert yanit.status_code == 200
    assert "Kampüs Kütüphane Sistemi" in yanit.get_data(as_text=True)


@pytest.mark.parametrize("adres", ["/uyelik/", "/katalog/", "/odunc/", "/ceza-rapor/"])
def test_modul_sayfalari_acilir(client, adres):
    assert client.get(adres).status_code == 200


def test_olmayan_sayfa_404_doner(client):
    assert client.get("/olmayan-sayfa").status_code == 404


def test_veritabani_tablolari_olusur(app):
    with app.app_context():
        tablolar = {
            satir["name"]
            for satir in get_db().execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        }
    assert {"kullanici", "kitap", "odunc", "ceza"} <= tablolar
