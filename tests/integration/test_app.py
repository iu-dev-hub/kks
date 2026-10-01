"""EXAMPLE integration tests using the Flask test client.

Tarayıcı açmadan HTTP istekleri gönderir; birim testlerden yavaş,
E2E testlerden çok daha hızlıdır.
"""

import pytest

from app.core.db import get_db


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Kampüs Kütüphane Sistemi" in response.get_data(as_text=True)


@pytest.mark.parametrize("url", ["/membership/", "/catalog/", "/loans/", "/fines-reports/"])
def test_module_pages_load(client, url):
    assert client.get(url).status_code == 200


def test_unknown_page_returns_404(client):
    assert client.get("/does-not-exist").status_code == 404


def test_database_tables_are_created(app):
    with app.app_context():
        tables = {
            row["name"]
            for row in get_db().execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        }
    assert {"users", "books", "loans", "fines"} <= tables
