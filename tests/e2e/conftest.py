"""E2E testleri için canlı sunucu.

Testler başlamadan uygulama boş bir test veritabanıyla rastgele bir portta
arka planda başlatılır. Playwright'ın `page.goto("/")` gibi göreli adresleri
bu sunucuya gider. Ayrıca sunucuyu elle başlatmanız gerekmez.
"""

import threading

import pytest
from werkzeug.serving import make_server

from app import create_app
from app.ortak.db import init_db


@pytest.fixture(scope="session")
def base_url(tmp_path_factory):
    veritabani = tmp_path_factory.mktemp("e2e") / "e2e.sqlite"
    app = create_app({"TESTING": True, "DATABASE": str(veritabani)})
    with app.app_context():
        init_db()

    sunucu = make_server("127.0.0.1", 0, app)
    is_parcacigi = threading.Thread(target=sunucu.serve_forever, daemon=True)
    is_parcacigi.start()
    yield f"http://127.0.0.1:{sunucu.server_port}"
    sunucu.shutdown()
