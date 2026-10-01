"""ÖRNEK uçtan uca (E2E) testleri: Playwright ile gerçek tarayıcıda.

Çalıştırma:
    pytest tests/e2e                  # tarayıcı görünmez (headless)
    pytest tests/e2e --headed         # tarayıcıyı görerek
    pytest tests/e2e --slowmo 500     # adımları yavaşlatarak

İpucu: Elemanları kullanıcının gördüğü şekilde bulun (get_by_role, get_by_label,
get_by_text). CSS sınıflarına bağlı testler tasarım değişince kırılır.
"""

import re

import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.e2e


def test_anasayfa_basligi(page: Page):
    page.goto("/")
    expect(page).to_have_title(re.compile("Ana Sayfa"))
    expect(page.get_by_role("heading", level=1)).to_contain_text("Hoş Geldiniz")


@pytest.mark.parametrize(
    ("menu", "adres", "ekip"),
    [
        ("Üyelik", "/uyelik/", "Ekip 1"),
        ("Katalog", "/katalog/", "Ekip 2"),
        ("Ödünç", "/odunc/", "Ekip 3"),
        ("Ceza ve Rapor", "/ceza-rapor/", "Ekip 4"),
    ],
)
def test_menuden_modullere_gecis(page: Page, menu, adres, ekip):
    page.goto("/")
    page.get_by_role("navigation", name="Ana menü").get_by_role("link", name=menu).click()

    expect(page).to_have_url(re.compile(re.escape(adres) + "$"))
    expect(page.get_by_role("heading", level=1)).to_have_text(menu)
    expect(page.get_by_text(ekip)).to_be_visible()
