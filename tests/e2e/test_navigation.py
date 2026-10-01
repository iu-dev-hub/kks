"""EXAMPLE end-to-end (E2E) tests with Playwright in a real browser.

Çalıştırma:
    pytest tests/e2e                  # tarayıcı görünmez (headless)
    pytest tests/e2e --headed         # tarayıcıyı görerek
    pytest tests/e2e --slowmo 500     # adımları yavaşlatarak

İpucu: Elemanları kullanıcının gördüğü şekilde bulun (get_by_role, get_by_label,
get_by_text). Arayüz Türkçe olduğu için testlerdeki metinler de Türkçedir.
"""

import re

import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.e2e


def test_home_page_title(page: Page):
    page.goto("/")
    expect(page).to_have_title(re.compile("Ana Sayfa"))
    expect(page.get_by_role("heading", level=1)).to_contain_text("Hoş Geldiniz")


@pytest.mark.parametrize(
    ("menu_label", "url", "team"),
    [
        ("Üyelik", "/membership/", "Team Membership"),
        ("Katalog", "/catalog/", "Team Catalog"),
        ("Ödünç", "/loans/", "Team Loans"),
        ("Ceza ve Rapor", "/fines-reports/", "Team Fines-Reports"),
    ],
)
def test_navigate_to_modules_from_menu(page: Page, menu_label, url, team):
    page.goto("/")
    page.get_by_role("navigation", name="Ana menü").get_by_role("link", name=menu_label).click()

    expect(page).to_have_url(re.compile(re.escape(url) + "$"))
    expect(page.get_by_role("heading", level=1)).to_have_text(menu_label)
    expect(page.get_by_text(team)).to_be_visible()
