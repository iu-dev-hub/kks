"""Date helpers (used by the loans and fines modules).

Bu dosya aynı zamanda bir ÖRNEKTİR: Küçük, saf (yan etkisiz) fonksiyonlar
ve bunlara ait birim testleri (tests/unit/test_dates.py) nasıl yazılır?
"""

from datetime import date, timedelta


def add_days(start: date, days: int) -> date:
    """Başlangıç tarihine verilen gün sayısını ekler.

    >>> add_days(date(2026, 10, 1), 14)
    datetime.date(2026, 10, 15)
    """
    if days < 0:
        raise ValueError("days must not be negative")
    return start + timedelta(days=days)


def days_overdue(due_date: date, return_date: date) -> int:
    """İadenin son tarihten kaç gün geç yapıldığını döndürür.

    Zamanında veya erken iade için 0 döner (BR-4.3: son gün iade gecikme sayılmaz).
    """
    return max((return_date - due_date).days, 0)
