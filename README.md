# Kampüs Kütüphane Sistemi (KKS)

**Yazılım Doğrulama ve Sınama** dersi ortak projesi
Yazılım Mühendisliği Bölümü · Dr. Öğr. Üyesi Hakan DUMAN

Kampüs Kütüphane Sistemi, üniversite kütüphanesinin web tabanlı yönetim uygulamasıdır.
Dört ekip, aynı ürünün farklı modülleri üzerinde Scrum ile birlikte çalışır.

- **Proje yönetimi (backlog, sprintler, hatalar):** Taiga — tree.taiga.io
- **Kod, kod incelemesi, CI:** Bu GitHub deposu

| Ekip | Modül | Klasör |
|---|---|---|
| Ekip 1 | Üyelik | `app/uyelik/` |
| Ekip 2 | Katalog | `app/katalog/` |
| Ekip 3 | Ödünç | `app/odunc/` |
| Ekip 4 | Ceza ve Rapor | `app/ceza_rapor/` |
| Tüm ekipler | Ortak kod | `app/ortak/` |

## Kurulum

Gerekenler: Python 3.12, Git, VS Code (önerilir)

```bash
# 1. Depoyu klonlayın
git clone https://github.com/iu-dev-hub/kks.git
cd kks

# 2. Sanal ortam oluşturun ve etkinleştirin
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt
python -m playwright install chromium

# 4. Veritabanını oluşturun
flask --app app init-db

# 5. Uygulamayı çalıştırın: http://127.0.0.1:5000
python run.py
```

## Testleri çalıştırma

```bash
pytest                                   # tüm testler
pytest tests/unit                        # yalnızca birim testleri
pytest tests/integration                 # yalnızca entegrasyon testleri
pytest tests/e2e                         # yalnızca uçtan uca testler
pytest tests/e2e --headed --slowmo 500   # tarayıcıyı görerek, yavaşlatarak
pytest --cov --cov-report=html           # kapsama raporu (htmlcov/index.html)
```

Kod stili ve statik analiz:

```bash
ruff check .         # sorunları göster
ruff check . --fix   # düzeltilebilenleri düzelt
ruff format .        # kodu biçimlendir
```

## Proje yapısı

```text
app/
  ortak/          Ortak kod: veritabanı, şema, yardımcı fonksiyonlar
  uyelik/         Ekip 1   (routes.py: sayfalar, servis.py: iş kuralları)
  katalog/        Ekip 2
  odunc/          Ekip 3
  ceza_rapor/     Ekip 4
  templates/      HTML şablonları (her modülün kendi klasörü var)
tests/
  unit/           Birim testleri (pytest)
  integration/    Entegrasyon testleri (Flask test istemcisi)
  e2e/            Uçtan uca testler (Playwright)
docs/             Ürün ve süreç belgeleri
```

## Belgeler

Çalışmaya başlamadan önce mutlaka okuyun:

- [Çalışma kuralları](CONTRIBUTING.md): Dal, commit, PR akışı ve yapay zekâ kuralları
- [Rol dağılımı](ROLLER.md)
- [Ürün vizyonu](docs/urun_vizyonu.md) ve [iş kuralları](docs/is_kurallari.md)
- [Arayüz sözleşmesi](docs/arayuz_sozlesmesi.md): Modüller arası fonksiyonlar
- [Hazır ve Bitti tanımı](docs/hazir_ve_bitti_tanimi.md)
- [Proje yönetimi](docs/proje_yonetimi.md): Taiga kullanımı ve GitHub bağlantısı
- [Hata raporu şablonu](docs/hata_raporu_sablonu.md): Taiga'ya kopyalanacak şablon

---

*ISTQB® kavramları, ISTQB® CTFL Syllabus v4.0.1 temel alınarak kullanılmıştır.*
