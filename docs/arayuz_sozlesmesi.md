# Arayüz Sözleşmesi

Modüllerin birbirinden kullanacağı fonksiyonlar burada tanımlanır.
**Sprint 2'de Scrum Master'lar birlikte doldurur.**

Kurallar:

- Bir modül, başka bir modülün yalnızca burada listelenen fonksiyonlarını çağırabilir.
- Fonksiyonlar ilgili modülün `servis.py` dosyasında yer alır.
- Sözleşmedeki bir imzayı değiştirmek için önce Scrum of Scrums'ta karar alınır,
  sonra bu belge ve kod **aynı PR'da** güncellenir.
- Karşı ekip fonksiyonu henüz yazmadıysa, beklerken testlerde sahte (mock) bir
  sürüm kullanın.

## Örnek tanım biçimi

```python
# Sağlayan: Ekip 1 (app/uyelik/servis.py)
# Kullanan: Ekip 3, Ekip 4
def kullanici_getir(kullanici_id: int) -> dict | None:
    """Kullanıcıyı döndürür; yoksa None.

    Dönen sözlük: {"id": int, "eposta": str, "ad_soyad": str, "rol": str}
    rol değerleri: "ogrenci" | "akademisyen" | "gorevli"
    """
```

## 1. Üyelik (Ekip 1) tarafından sağlananlar

<!-- Doldurun -->

## 2. Katalog (Ekip 2) tarafından sağlananlar

<!-- Doldurun -->

## 3. Ödünç (Ekip 3) tarafından sağlananlar

<!-- Doldurun -->

## 4. Ceza ve Rapor (Ekip 4) tarafından sağlananlar

<!-- Doldurun -->

## Değişiklik geçmişi

| Tarih | Değişiklik | Karar veren toplantı |
|---|---|---|
