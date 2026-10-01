"""Tarih yardımcıları (ödünç ve ceza modülleri tarafından kullanılır).

Bu dosya aynı zamanda bir ÖRNEKTİR: Küçük, saf (yan etkisiz) fonksiyonlar
ve bunlara ait birim testleri (tests/unit/test_tarih.py) nasıl yazılır?
"""

from datetime import date, timedelta


def gun_ekle(baslangic: date, gun: int) -> date:
    """Başlangıç tarihine verilen gün sayısını ekler.

    >>> gun_ekle(date(2026, 10, 1), 14)
    datetime.date(2026, 10, 15)
    """
    if gun < 0:
        raise ValueError("Gün sayısı negatif olamaz")
    return baslangic + timedelta(days=gun)


def gecikme_gunu(son_tarih: date, iade_tarihi: date) -> int:
    """İadenin son tarihten kaç gün geç yapıldığını döndürür.

    Zamanında veya erken iade için 0 döner.
    """
    fark = (iade_tarihi - son_tarih).days
    return max(fark, 0)
