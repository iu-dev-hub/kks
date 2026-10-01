"""ÖRNEK birim testi: app/ortak/tarih.py

Bu dosya, derste öğrenilen tekniklerin pytest'e nasıl aktarıldığını gösterir:
- pytest.mark.parametrize ile birden çok test durumu tek fonksiyonda
- Sınır değer analizi: 0 sınırının hemen altı, kendisi ve hemen üstü
- Hata durumlarının pytest.raises ile test edilmesi
"""

from datetime import date

import pytest

from app.ortak.tarih import gecikme_gunu, gun_ekle

SON_TARIH = date(2026, 10, 15)


@pytest.mark.parametrize(
    ("gun", "beklenen"),
    [
        (0, date(2026, 10, 1)),  # aynı gün
        (14, date(2026, 10, 15)),  # öğrenci ödünç süresi
        (30, date(2026, 10, 31)),  # akademisyen ödünç süresi (ay sonu)
        (31, date(2026, 11, 1)),  # ay geçişi
    ],
)
def test_gun_ekle(gun, beklenen):
    assert gun_ekle(date(2026, 10, 1), gun) == beklenen


def test_gun_ekle_yil_gecisi():
    assert gun_ekle(date(2026, 12, 25), 14) == date(2027, 1, 8)


def test_gun_ekle_negatif_gun_hata_verir():
    with pytest.raises(ValueError):
        gun_ekle(date(2026, 10, 1), -1)


@pytest.mark.parametrize(
    ("iade_tarihi", "beklenen"),
    [
        (date(2026, 10, 14), 0),  # sınırın hemen altı: bir gün erken
        (date(2026, 10, 15), 0),  # tam sınır: son gün iade
        (date(2026, 10, 16), 1),  # sınırın hemen üstü: bir gün gecikme
        (date(2026, 11, 15), 31),  # uzun gecikme
    ],
)
def test_gecikme_gunu_sinir_degerleri(iade_tarihi, beklenen):
    assert gecikme_gunu(SON_TARIH, iade_tarihi) == beklenen
