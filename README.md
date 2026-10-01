# Kampüs Kütüphane Sistemi (KKS)

**Yazılım Doğrulama ve Sınama** dersi ortak projesi
Yazılım Mühendisliği Bölümü · Dr. Öğr. Üyesi Hakan DUMAN

Kampüs Kütüphane Sistemi, üniversite kütüphanesinin web tabanlı yönetim uygulamasıdır.
Dört ekip, aynı ürünün farklı modülleri üzerinde Scrum ile birlikte çalışır.

- **Proje yönetimi (backlog, sprintler, hatalar):** Taiga — tree.taiga.io
- **Kod, kod incelemesi, CI:** Bu GitHub deposu

> Bu depo bilerek **sade** başlıyor. Modülleri, veritabanını ve ekip anlaşmalarını
> dönem boyunca siz geliştireceksiniz. Depodaki her dosyayı okuyup anlayabilirsiniz;
> anlamadığınız bir şey varsa sorun.

| Ekip (GitHub team) | Modül | Klasör | Ne zaman? |
|---|---|---|---|
| `team-membership` | Üyelik | `app/membership/` | Sprint 1 |
| `team-catalog` | Katalog | `app/catalog/` | Sprint 1 |
| `team-loans` | Ödünç | `app/loans/` | Sprint 1 |
| `team-fines-reports` | Ceza ve Rapor | `app/fines_reports/` | Sprint 1 |
| Tüm ekipler | Ortak kod | `app/core/` | Mevcut |

**İsimlendirme kuralı:** Kod, dosya, klasör, veritabanı, URL, dal ve commit adları
**İngilizce**; kullanıcı arayüzü ve belgelerin içeriği **Türkçe**dir
(terimler: [docs/glossary.md](docs/glossary.md)).

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
pytest tests/unit                        # birim testleri
pytest tests/integration                 # entegrasyon testleri
pytest tests/e2e --headed                # uçtan uca testler, tarayıcıyı görerek
pytest --cov --cov-report=html           # kapsama raporu (htmlcov/index.html)
ruff check .                             # statik analiz
```

## Proje yapısı

```text
app/
  __init__.py      Uygulama fabrikası (modüller burada kaydedilir)
  core/            Ortak kod: veritabanı, şema (schema.sql), yardımcı fonksiyonlar
  templates/       HTML şablonları (base.html: ortak sayfa düzeni)
  static/          CSS
tests/
  unit/            Birim testleri (pytest) — örnek: test_dates.py
  integration/     Entegrasyon testleri (Flask test istemcisi)
  e2e/             Uçtan uca testler (Playwright)
docs/              Ürün belgeleri ve ekip anlaşmaları
```

## Dönem boyunca neler eklenecek?

| Sprint | Siz eklersiniz | CI'a eklenen kalite kapısı |
|---|---|---|
| 1 | Modül klasörleri ve ilk sayfalar, `docs/definition-of-ready-and-done.md` | Birim ve entegrasyon testleri (mevcut) |
| 2 | Veritabanı tabloları (`schema.sql`), `docs/interface-contract.md` | |
| 4 | | Statik analiz (ruff) |
| 6 | | Uçtan uca testler (Playwright) |
| 8 | | Kod kapsama eşiği |

## Belgeler

- [CONTRIBUTING.md](CONTRIBUTING.md): Çalışma kuralları, Taiga, dal ve commit, yeni modül ekleme
- [ROLES.md](ROLES.md): Rol dağılımı ve sorumluluklar
- [docs/product-vision.md](docs/product-vision.md): Ürün vizyonu (müşteri)
- [docs/business-rules.md](docs/business-rules.md): İş kuralları (müşteri)
- [docs/bug-report-template.md](docs/bug-report-template.md): Taiga hata raporu şablonu
- [docs/glossary.md](docs/glossary.md): İngilizce–Türkçe terimler sözlüğü

---

*ISTQB® kavramları, ISTQB® CTFL Syllabus v4.0.1 temel alınarak kullanılmıştır.*
