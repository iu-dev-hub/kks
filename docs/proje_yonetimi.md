# Proje Yönetimi: Taiga + GitHub

Bu derste iş takibi **Taiga**'da, kod ise **GitHub**'da yapılır. Bu düzen, sektörde
yaygın olan "Jira + GitHub" kullanımının birebir karşılığıdır.

| Kavram | Taiga | Jira'daki karşılığı |
|---|---|---|
| Ürün backlog'u | Backlog | Backlog |
| Büyük özellik | Epic | Epic |
| Kullanıcı hikâyesi | User Story | Story |
| Alt iş | Task | Sub-task |
| Hata | Issue (tür: Bug) | Bug |
| Sprint | Sprint | Sprint |
| Sprint panosu | Taskboard | Scrum board |
| Tahmin | Points | Story points |
| İlerleme | Burndown | Burndown chart |
| Kodla bağlantı | GitHub webhook (`TG-42`) | GitHub for Jira (`KKS-42`) |

---

## 1. Taiga projesinin kurulumu (öğretim üyesi)

### Proje

> Taiga'nın güncel arayüzünde yönetim menüsü sol menünün en altındaki
> **Settings** (dişli simgesi) altındadır. Bu menüyü yalnızca proje yöneticileri görür.

1. **tree.taiga.io** adresinde hesap açın.
2. **New project → Scrum** şablonunu seçin.
   - Ad: `Kampüs Kütüphane Sistemi`
   - Görünürlük: **Private (özel)**. Ücretsiz planda 1 özel proje hakkı vardır.
3. **Settings → Project → Modules:** Epics, Scrum, Issues ve Wiki açık; Kanban kapalı.

### Ücretsiz plan sınırları

- 1 özel + 1 herkese açık proje, **sınırsız kullanıcı**
- Toplam **10 MB** depolama: **Taiga'ya dosya eklenmez** (bkz. Bölüm 4)

### Roller ve yetkiler (Settings → Permissions)

**Roller:** Taiga'nın varsayılanlarından **UX** ve **Design** silinir; **Product Owner**,
**Back**, **Front** ve **Stakeholder** korunur; **Scrum Master** ve **Testçi** eklenir.
Proje yöneticisi (admin) yalnızca öğretim üyesidir (Settings → Members).

PO = Product Owner, SM = Scrum Master, Test = Testçi, Stk = Stakeholder ·
✓ açık, – kapalı

| Modül | Yetki | PO | SM | Back | Front | Test | Stk |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| **Epics** | Görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Ekle | ✓ | ✓ | – | – | – | – |
| | Düzenle | ✓ | ✓ | – | – | – | – |
| | Yorum yap | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Sil | ✓ | – | – | – | – | – |
| **Sprints** | Görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Ekle / Düzenle / Sil | – | ✓ | – | – | – | – |
| **User Stories** | Görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Ekle | ✓ | ✓ | – | – | – | – |
| | Düzenle | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Yorum yap | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Sil | ✓ | – | – | – | – | – |
| **Tasks** | Görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Ekle / Düzenle / Yorum yap | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Sil | – | ✓ | – | – | – | – |
| **Issues** | Görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Ekle / Düzenle / Yorum yap | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Sil | – | – | – | – | – | – |
| **Wiki** | Sayfaları görüntüle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| | Sayfa ekle / düzenle | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| | Sayfa sil | – | ✓ | – | – | – | – |
| | Bağlantı ekle / sil | ✓ | ✓ | – | – | – | – |
| **Tahmin** | Puan verir (estimation) | – | – | ✓ | – | – | – |

Gerekçeler:

- **Hikâyeyi PO ekler ve siler.** SM, PO yokken ekleyebilir ama silemez. Ekip üyeleri
  hikâyeleri yalnızca düzenler, çünkü Taiga'da durum değiştirmek düzenleme yetkisi ister.
- **Sprintleri SM yönetir.**
- **Hata kayıtları silinmez,** gerekiyorsa "Reddedildi" durumuna alınır (izlenebilirlik).
  Yanlış açılan kaydı yalnızca admin siler.
- **Görevleri SM siler;** panonun düzeni onun sorumluluğundadır.
- **Stakeholder yalnızca izler** (bölüm başkanı, konuklar).
- **Puanı yalnızca Back girer.** Taiga puan veren rollerin tahminlerini toplar; ekip
  planning poker ile ortak puanı belirler, Back bu sayıyı girer.
- "Bitti'ye yalnızca PO taşır" ve "Testte'den testçi ilerletir" kuralları Taiga'da teknik
  olarak zorlanamaz; ekip kuralıdır ve geçmiş (history) kaydından izlenir.
- **Eksik üye:** Taiga'da öğretim üyesi admin olduğu için her rolün işini yapabilir;
  ayrıca rol ataması gerekmez.

### Durumlar (Settings → Attributes → Statuses)

**User Story durumları** (sırasıyla):

| Durum | Kapalı mı? | Anlamı |
|---|---|---|
| Yeni | Hayır | PO yazıyor |
| Hazır | Hayır | Hazır Tanımı sağlandı, sprinte alınabilir |
| Yapılıyor | Hayır | Geliştirme sürüyor |
| İncelemede | Hayır | PR açıldı, kod incelemesi bekleniyor |
| Testte | Hayır | PR birleşti, testçi doğruluyor |
| Bitti | **Evet** | PO kabul etti |

**Task durumları:** Yeni, Yapılıyor, İncelemede, Kapandı (kapalı)

**Issue (hata) ayarları:**

- Türler: `Bug`, `İyileştirme`, `Soru`
- Önem derecesi (severity): `Kritik`, `Yüksek`, `Orta`, `Düşük`
- Öncelik (priority): `Yüksek`, `Normal`, `Düşük` (PO belirler)
- Durumlar: Yeni, Kabul edildi, Düzeltiliyor, Test edilecek, Kapandı (kapalı),
  Reddedildi (kapalı), Tekrar açıldı

### Puan ölçeği (Settings → Attributes → Points)

`?`, `1`, `2`, `3`, `5`, `8`. 8'den büyük hikâye bölünmelidir.

### Ekipleri ayırma

- **Etiketler (tags):** `ekip-1`, `ekip-2`, `ekip-3`, `ekip-4`, `ortak`
  (her birine farklı renk verin)
- **Özel alan (Settings → Attributes → Custom fields → User stories):** `Ekip`
- Her ekip backlog ve taskboard'u kendi etiketine göre filtreler.
- Bağımlılıklar hikâye açıklamasında diğer hikâyenin numarasıyla belirtilir
  (ör. "Bağımlı: #17, Ekip 1").

### Üyeler (Settings → Members → New member)

Öğrencileri e-posta ile davet edin ve rollerini atayın. Öğrencilerin Taiga'daki e-posta
adresi, `git config user.email` ile aynı olursa commit'ler doğru kişiyle eşleşir.

### Sprintler

Backlog ekranında **New sprint** ile 1 haftalık sprintler oluşturun. Başlangıç ve bitiş
tarihi uygulama dersi günüdür. Sprint kapanınca tamamlanmayan hikâyeler sonraki sprinte
veya backlog'a taşınır.

---

## 2. Taiga–GitHub bağlantısı (öğretim üyesi)

1. Taiga: **Settings → Integrations → GitHub**. Burada bir **Payload URL** ve
   **Secret key** göreceksiniz.
2. GitHub: Depo → **Settings → Webhooks → Add webhook**
   - Payload URL: Taiga'daki adres
   - Content type: `application/json`
   - Secret: Taiga'daki anahtar
   - **Which events?** → *Let me select individual events* → **yalnızca Pushes**
3. Kaydedin ve deneyin:

```bash
git commit --allow-empty -m "test: taiga baglanti denemesi (TG-1)"
git push
```

Taiga'da #1 numaralı kayıtta commit'in yorum olarak göründüğünü kontrol edin.

> **Neden yalnızca Pushes?** Taiga'nın GitHub entegrasyonu GitHub issue'larını da
> Taiga'ya aktarabilir. "Hata Ekleri" kayıtlarımızın Taiga'ya kopyalanmasını ve
> karışıklık yaratmasını istemiyoruz.

---

## 3. Günlük kullanım (öğrenciler)

| Kim? | Taiga'da ne yapar? |
|---|---|
| PO | Hikâyeleri ve kabul kriterlerini yazar, önceliklendirir, kabul eder (**Bitti**) |
| SM | Sprint açar/kapatır, panoyu düzenli tutar, burndown'ı review'da gösterir |
| Back | Görevleri üstlenir, durumları günceller, ekibin ortak puanını girer |
| Front | Görevleri üstlenir, durumları günceller |
| Testçi | Hikâyeleri **Testte**'den ileri/geri taşır, hata kaydı açar |

**Taiga numarası GitHub'da:** Taiga'da `#42` → GitHub'da `TG-42`
(ayrıntılar: `CONTRIBUTING.md`, Bölüm 3)

---

## 4. Dosyalar: Taiga'ya değil, GitHub'a

Taiga'nın ücretsiz planında toplam 10 MB alan var. Bu yüzden:

- **Ekran görüntüsü, log, video:** GitHub'da *Issues → New issue → Hata Ekleri*
  şablonuyla bir kayıt açın, dosyaları oraya sürükleyin, bağlantıyı Taiga'ya yapıştırın.
- **PR ile ilgili görseller:** Doğrudan PR'a yorum olarak ekleyin.
- **CI'da başarısız E2E testinin izi:** GitHub Actions çalıştırmasının bağlantısını verin.

---

## Ek: Diğer araçlar

Taiga'ya erişim sorunu yaşanırsa aynı yapı **GitHub Projects** ile de kurulabilir
(iteration alanı = sprint, single select alanı = ekip/durum). Gelecek yıllarda bütçe veya
lisans sağlanırsa **Jira** ile de aynı düzen kullanılabilir; bu durumda `TG-42` yerine
`KKS-42` biçimi ve "GitHub for Jira" uygulaması kullanılır.
