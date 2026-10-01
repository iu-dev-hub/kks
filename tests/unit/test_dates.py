"""EXAMPLE unit tests for app/core/dates.py

Bu dosya, derste öğrenilen tekniklerin pytest'e nasıl aktarıldığını gösterir:
- pytest.mark.parametrize ile birden çok test durumu tek fonksiyonda
- Sınır değer analizi: sınırın hemen altı, kendisi ve hemen üstü
- Hata durumlarının pytest.raises ile test edilmesi
"""

from datetime import date

import pytest

from app.core.dates import add_days, days_overdue

DUE_DATE = date(2026, 10, 15)


@pytest.mark.parametrize(
    ("days", "expected"),
    [
        (0, date(2026, 10, 1)),  # aynı gün
        (14, date(2026, 10, 15)),  # öğrenci ödünç süresi (BR-3.2)
        (30, date(2026, 10, 31)),  # akademisyen ödünç süresi, ay sonu
        (31, date(2026, 11, 1)),  # ay geçişi
    ],
)
def test_add_days(days, expected):
    assert add_days(date(2026, 10, 1), days) == expected


def test_add_days_across_year_boundary():
    assert add_days(date(2026, 12, 25), 14) == date(2027, 1, 8)


def test_add_days_rejects_negative_days():
    with pytest.raises(ValueError):
        add_days(date(2026, 10, 1), -1)


@pytest.mark.parametrize(
    ("return_date", "expected"),
    [
        (date(2026, 10, 14), 0),  # sınırın hemen altı: bir gün erken
        (date(2026, 10, 15), 0),  # tam sınır: son gün iade (BR-4.3)
        (date(2026, 10, 16), 1),  # sınırın hemen üstü: bir gün gecikme
        (date(2026, 11, 15), 31),  # uzun gecikme
    ],
)
def test_days_overdue_boundary_values(return_date, expected):
    assert days_overdue(DUE_DATE, return_date) == expected
