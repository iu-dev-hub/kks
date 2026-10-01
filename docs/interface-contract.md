# Interface Contract (Arayüz Sözleşmesi)

Modüllerin birbirinden kullanacağı fonksiyonlar burada tanımlanır.
**Sprint 2'de Scrum Master'lar birlikte doldurur.**

Kurallar:

- Bir modül, başka bir modülün yalnızca burada listelenen fonksiyonlarını çağırabilir.
- Fonksiyonlar ilgili modülün `services.py` dosyasında yer alır.
- Sözleşmedeki bir imzayı değiştirmek için önce Scrum of Scrums'ta karar alınır,
  sonra bu belge ve kod **aynı PR'da** güncellenir.
- Karşı ekip fonksiyonu henüz yazmadıysa, beklerken testlerde sahte (mock) bir
  sürüm kullanın.

## Örnek tanım biçimi

```python
# Provider: Team Membership (app/membership/services.py)
# Consumers: Team Loans, Team Fines-Reports
def get_user(user_id: int) -> dict | None:
    """Kullanıcıyı döndürür; yoksa None.

    Dönen sözlük: {"id": int, "email": str, "full_name": str, "role": str}
    role değerleri: "student" | "academic" | "librarian"
    """
```

## 1. Provided by Team Membership (`app/membership/services.py`)

<!-- Doldurun -->

## 2. Provided by Team Catalog (`app/catalog/services.py`)

<!-- Doldurun -->

## 3. Provided by Team Loans (`app/loans/services.py`)

<!-- Doldurun -->

## 4. Provided by Team Fines-Reports (`app/fines_reports/services.py`)

<!-- Doldurun -->

## Change log (Değişiklik geçmişi)

| Tarih | Değişiklik | Karar veren toplantı |
|---|---|---|
