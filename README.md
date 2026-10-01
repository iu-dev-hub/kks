# Kampüs Kütüphane Sistemi (KKS)

**Yazılım Doğrulama ve Sınama** dersi ortak projesi
Yazılım Mühendisliği Bölümü · Dr. Öğr. Üyesi Hakan DUMAN

Kampüs Kütüphane Sistemi, üniversite kütüphanesinin web tabanlı yönetim uygulamasıdır.
Dört ekip, aynı ürünün farklı modülleri üzerinde Scrum ile birlikte çalışır.

- **Proje yönetimi (backlog, sprintler, hatalar):** Taiga — tree.taiga.io
- **Kod, kod incelemesi, CI:** Bu GitHub deposu

| Ekip (GitHub team) | Modül | Klasör |
|---|---|---|
| `team-membership` | Üyelik | `app/membership/` |
| `team-catalog` | Katalog | `app/catalog/` |
| `team-loans` | Ödünç | `app/loans/` |
| `team-fines-reports` | Ceza ve Rapor | `app/fines_reports/` |
| Tüm ekipler | Ortak kod | `app/core/` |

> **İsimlendirme kuralı:** Kod, dosya, klasör, veritabanı, URL, dal ve commit adları
> **İngilizce**; kullanıcı arayüzü ve belgelerin içeriği **Türkçe**dir.
> Terimler için: [docs/glossary.md](docs/glossary.md)

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
  core/            Ortak kod: veritabanı, şema, yardımcı fonksiyonlar
  membership/      Üyelik       (routes.py: sayfalar, services.py: iş kuralları)
  catalog/         Katalog
  loans/           Ödünç
  fines_reports/   Ceza ve Rapor
  templates/       HTML şablonları (her modülün kendi klasörü var)
  static/          CSS ve diğer statik dosyalar
tests/
  unit/            Birim testleri (pytest)
  integration/     Entegrasyon testleri (Flask test istemcisi)
  e2e/             Uçtan uca testler (Playwright)
docs/              Ürün ve süreç belgeleri
```

## Belgeler

Çalışmaya başlamadan önce mutlaka okuyun:

- [CONTRIBUTING.md](CONTRIBUTING.md): Dal, commit, PR akışı ve yapay zekâ kuralları
- [ROLES.md](ROLES.md): Rol dağılımı ve sorumluluklar
- [docs/product-vision.md](docs/product-vision.md) ve [docs/business-rules.md](docs/business-rules.md)
- [docs/interface-contract.md](docs/interface-contract.md): Modüller arası fonksiyonlar
- [docs/definition-of-ready-and-done.md](docs/definition-of-ready-and-done.md)
- [docs/project-management.md](docs/project-management.md): Taiga kullanımı ve GitHub bağlantısı
- [docs/bug-report-template.md](docs/bug-report-template.md): Taiga'ya kopyalanacak hata şablonu
- [docs/glossary.md](docs/glossary.md): İngilizce–Türkçe terimler sözlüğü

---

*ISTQB® kavramları, ISTQB® CTFL Syllabus v4.0.1 temel alınarak kullanılmıştır.*
