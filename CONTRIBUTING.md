# Çalışma Kuralları

Bu belge, gerçek bir yazılım ekibinin günlük çalışma düzenini taklit eder:
iş takibi Taiga'da (sektörde çoğunlukla Jira), kod GitHub'da.
Kurallar CI ve dal koruma ayarlarıyla da desteklenir; çoğunu atlamak teknik olarak mümkün değildir.

## 1. Hangi iş nerede yapılır?

| Taiga (tree.taiga.io) | GitHub |
|---|---|
| Backlog, epic'ler, kullanıcı hikâyeleri | Kod ve pull request'ler |
| Sprintler ve görev panosu (taskboard) | Kod incelemesi |
| Görevler (task) | CI sonuçları |
| Hata raporları (Issues, tür: Bug) | Ekran görüntüleri, loglar, test izleri |
| Burndown grafikleri, Wiki | Discussions: asenkron günlük toplantı |

**Taiga'ya dosya eklemeyin.** Ücretsiz planın toplam depolama alanı 10 MB'tır.
Dosyaları GitHub'a yükleyin (ilgili PR'a yorum olarak veya "Hata Ekleri"
şablonuyla açılan bir GitHub kaydına), Taiga'ya yalnızca bağlantısını yapıştırın.

## 2. Bir işin yolculuğu

1. **PO**, Taiga'da kullanıcı hikâyesini kabul kriterleriyle yazar (ör. Taiga'da **#42**).
2. **Sprint planlamada** hikâye sprinte alınır, puanlanır ve görevlere bölünür
   (Hazır ve Bitti Tanımı: `docs/definition-of-ready-and-done.md`, Sprint 1'de birlikte yazılır).
3. **Geliştirici** görevi üstlenir (Taiga'da kendine atar), GitHub'da dal açar.
4. Kodu ve birim testlerini yazar, **PR** açar; hikâyeyi Taiga'da **İncelemede**'ye taşır.
5. **CI** testleri otomatik çalıştırır. Kırmızıysa birleştirme yapılamaz.
6. **Bir ekip arkadaşı** kodu inceler. Başka ekibin klasörüne dokunulduysa o ekip de onaylar.
7. PR birleşince geliştirici hikâyeyi **Testte**'ye taşır.
8. **Testçi** kabul kriterlerini E2E testleriyle doğrular. Hata bulursa Taiga'da hata
   kaydı açar ve hikâyeyi **Yapılıyor**'a geri alır.
9. **PO** sonucu kontrol eder ve hikâyeyi **Bitti**'ye taşır (= kabul).

## 3. İsimlendirme, dallar ve commit mesajları

### İsimlendirme

| Ne? | Dil | Biçim | Örnek |
|---|---|---|---|
| Klasör, modül, Python dosyası | İngilizce | `snake_case` | `app/loans/services.py` |
| Fonksiyon, değişken | İngilizce | `snake_case` | `can_borrow(user, active_loans)` |
| Sınıf | İngilizce | `PascalCase` | `LoanPolicy` |
| Sabit | İngilizce | `UPPER_SNAKE_CASE` | `MAX_LOANS_STUDENT = 3` |
| Veritabanı tablo ve sütunu | İngilizce | `snake_case`, tablo çoğul | `loans.due_date` |
| URL | İngilizce | `kebab-case` | `/fines-reports/` |
| Belge dosyası | İngilizce | `kebab-case.md` | `docs/business-rules.md` |
| Test fonksiyonu | İngilizce | `test_<ne>_<koşul>` | `test_fine_is_capped_at_50` |
| **Kullanıcı arayüzü metni** | **Türkçe** | | "Ödünç limitinize ulaştınız" |
| Kod içi yorum, belge içeriği | Türkçe | | |

Python adlandırması PEP 8'e uyar; `ruff` bunun bir kısmını otomatik kontrol eder.
Türkçe karşılıklar için [docs/glossary.md](docs/glossary.md) dosyasına bakın.

### Taiga numarası

Taiga'da **#42** olarak görünen kayıt, GitHub tarafında her zaman **TG-42** olarak yazılır.
Commit mesajında `TG-42` geçtiğinde commit, Taiga'daki kaydın geçmiş panelinde görünür.

> GitHub'da `#42` yazmayın: GitHub bunu kendi issue numarası sanar.
> `TG-42`'den sonra `#closed` gibi bir durum da yazmayın: Taiga hikâyeyi otomatik
> kapatır, oysa hikâyeyi yalnızca PO kapatmalıdır.

### Dal (branch) adları

```text
<type>/TG-<number>-<short-description>
```

| Tür | Kullanım | Örnek |
|---|---|---|
| `feature/` | Yeni özellik | `feature/TG-42-student-loan-limit` |
| `bugfix/` | Hata düzeltme | `bugfix/TG-57-fine-cap` |
| `hotfix/` | Canlıdaki acil hata | `hotfix/TG-80-login-crash` |
| `test/` | Yalnızca test ekleme | `test/TG-61-loan-boundary-tests` |
| `docs/` | Yalnızca belge | `docs/TG-12-interface-contract` |
| `chore/` | Bakım, yapılandırma | `chore/update-dependencies` |

Kısa açıklama İngilizce, küçük harf ve tire ile yazılır.

### Commit mesajları: Conventional Commits

Uluslararası **Conventional Commits** standardını kullanıyoruz:

```text
<type>(<scope>): <description> (TG-<number>)
```

| Tür | Anlamı |
|---|---|
| `feat` | Yeni özellik |
| `fix` | Hata düzeltme |
| `test` | Test ekleme veya değiştirme |
| `docs` | Belge değişikliği |
| `refactor` | Davranışı değiştirmeyen kod iyileştirmesi |
| `style` | Biçimlendirme (davranış değişmez) |
| `chore` | Bakım, bağımlılık, yapılandırma |
| `ci` | CI ayarları |

`scope` isteğe bağlıdır ve modül adıdır: `membership`, `catalog`, `loans`, `fines`, `core`.
Açıklama İngilizce, küçük harfle başlar, emir kipindedir ve sonunda nokta yoktur.

```text
feat(loans): add student loan limit check (TG-42)
fix(fines): cap overdue fine at 50 TL (TG-57)
test(loans): add boundary value tests for loan limit (TG-61)
docs: update interface contract for user lookup (TG-12)
```

**PR başlığı** commit biçimini izler: `feat(loans): add student loan limit check (TG-42)`

## 4. Pull request kuralları

- Her PR **tek bir işi** kapsar. Küçük PR'lar daha hızlı incelenir.
- PR şablonundaki **Taiga numarasını** doldurun.
- **Test içermeyen PR onaylanmaz.**
- Kendi PR'ınızı onaylayamazsınız.
- Başka bir ekibin testini bozduysanız testi silmeyin; o ekiple konuşun.

## 5. Kod incelemesi (code review) yaparken

- Kod, kabul kriterlerini karşılıyor mu?
- Sınır değerler test edilmiş mi? (ör. tam 3 kitap, tam 50 TL)
- Hata durumları ele alınmış mı?
- Kodu anlayabiliyor musunuz? Anlayamıyorsanız soru sorun.
- Eleştiriyi koda yapın, kişiye değil.

## 6. Soft vibe coding: Yapay zekâ kuralları

1. **Açıklayamadığın kodu gönderme.** Sprint review'da kodunuzun herhangi bir bölümünü
   açıklamanız istenebilir.
2. **Kod testleriyle birlikte gelir.** Yapay zekâya test yazdırabilirsiniz, ama testleri
   siz kontrol edersiniz.
3. **Şeffaf ol.** PR şablonundaki "Yapay zekâ kullanımı" bölümünü doldurun.
4. **Gizli bilgi paylaşma.** Şifre, anahtar veya kişisel veriyi yapay zekâya yapıştırmayın.
5. **Önerilen paketleri doğrula.** Yeni bir paket eklemeden önce PyPI'da gerçekten var
   olduğunu ve güvenilir olduğunu kontrol edin. `requirements.txt` değişikliği öğretim
   üyesinin onayını gerektirir.
6. **Başka ekibin koduna dokunmadan önce sor.**

## 7. Test tasarlarken: Önce teknik, sonra yapay zekâ

1. Derste öğrendiğiniz tekniği uygulayarak test durumlarını **kendiniz** çıkarın.
2. Aynı gereksinim için yapay zekâdan test senaryosu isteyin.
3. Karşılaştırın: Kim neyi kaçırdı?
4. En iyi kümeyi birleştirip otomatikleştirin.

## 8. Asenkron günlük toplantı

Her öğrenci haftada **en az 2 kez** ekibinin Discussions başlığına yazar:

1. Son yazımdan bu yana ne yaptım?
2. Şimdi ne yapacağım?
3. Önümde bir engel var mı?

## 9. Taiga'da günlük kullanım

**Hikâye durumları:** Yeni → Hazır → Yapılıyor → İncelemede → Testte → **Bitti**

| Geçiş | Kim yapar? |
|---|---|
| Yeni → Hazır | PO (Hazır Tanımı sağlandığında) |
| Hazır → Yapılıyor | Geliştirici (görevi üstlenince) |
| Yapılıyor → İncelemede | Geliştirici (PR açınca) |
| İncelemede → Testte | Geliştirici (PR birleşince) |
| Testte → Yapılıyor | Testçi (hata bulursa, hata kaydıyla birlikte) |
| Testte → **Bitti** | **Yalnızca PO** (kabul) |

| Rol | Taiga'da ne yapar? |
|---|---|
| Product Owner | Hikâyeleri ve kabul kriterlerini yazar, sıralar, kabul eder |
| Scrum Master | Sprint açar/kapatır, panoyu düzenli tutar, burndown'ı review'da gösterir |
| Back / Front | Görevleri (task) oluşturur ve üstlenir, durumları günceller |
| Testçi | Test görevlerini oluşturur, hata kaydı açar, hikâyeyi Testte'den ilerletir |

- Her hikâyeye ekibinizin etiketini ekleyin: `team-membership`, `team-catalog`,
  `team-loans`, `team-fines-reports` veya `core`.
- Puanı ekip planning poker ile belirler; Back geliştirici Taiga'ya girer.
- Hata kayıtları silinmez; gerekiyorsa **Reddedildi** durumuna alınır.
- **Taiga'ya dosya eklemeyin** (toplam 10 MB). Bkz. Bölüm 1.

## 10. Yeni modül ekleme (Sprint 1)

Her ekip Sprint 1'de kendi modülünü ekler. Klasör adları sabittir, çünkü
`CODEOWNERS` bu adlara göre tanımlıdır:

| Ekip | Klasör | Blueprint adı | URL öneki |
|---|---|---|---|
| team-membership | `app/membership/` | `membership` | `/membership` |
| team-catalog | `app/catalog/` | `catalog` | `/catalog` |
| team-loans | `app/loans/` | `loans` | `/loans` |
| team-fines-reports | `app/fines_reports/` | `fines_reports` | `/fines-reports` |

Bir modülde en az şunlar olmalı:

```text
app/<module>/__init__.py       # bp nesnesini dışa açar
app/<module>/routes.py         # sayfalar (Blueprint ve route'lar)
app/<module>/services.py       # iş kuralları (sayfalardan ayrı, kolay test edilir)
app/templates/<module>/index.html
tests/integration/test_<module>.py   # en az: modül sayfası açılıyor mu?
```

Ayrıca iki ortak dosyaya birer satır eklenir:

- `app/__init__.py`: modülün kaydı (`register_blueprint`)
- `app/templates/base.html`: menüdeki bağlantı

Bu iki dosyayı dört ekip aynı hafta değiştireceği için **birleştirme çatışması**
(merge conflict) yaşayabilirsiniz. Bu beklenen bir durumdur: Çatışmayı çözmek,
çok ekipli projelerin günlük işidir. Önce `main`'i kendi dalınıza alın
(`git pull origin main`), çatışan satırları birlikte düzeltin, testleri çalıştırın.

> İpucu: Yapay zekâdan modülü oluşturmasını isterken bu tabloyu ve
> `app/__init__.py` ile `base.html` dosyalarını bağlam olarak verin.
