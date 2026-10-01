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
2. **Sprint planlamada** hikâye sprinte alınır, puanlanır ve görevlere bölünür.
3. **Geliştirici** görevi üstlenir (Taiga'da kendine atar), GitHub'da dal açar.
4. Kodu ve birim testlerini yazar, **PR** açar; hikâyeyi Taiga'da **İncelemede**'ye taşır.
5. **CI** testleri otomatik çalıştırır. Kırmızıysa birleştirme yapılamaz.
6. **Bir ekip arkadaşı** kodu inceler. Başka ekibin klasörüne dokunulduysa o ekip de onaylar.
7. PR birleşince geliştirici hikâyeyi **Testte**'ye taşır.
8. **Testçi** kabul kriterlerini E2E testleriyle doğrular. Hata bulursa Taiga'da hata
   kaydı açar ve hikâyeyi **Yapılıyor**'a geri alır.
9. **PO** sonucu kontrol eder ve hikâyeyi **Bitti**'ye taşır (= kabul).

## 3. Taiga numarasını GitHub'da kullanma

Taiga'da **#42** olarak görünen kayıt, GitHub tarafında her zaman **TG-42** olarak yazılır.
Böylece commit'ler Taiga'daki kayda otomatik olarak bağlanır.

> GitHub'da `#42` yazmayın: GitHub bunu kendi issue numarası sanar.
> `TG-42`'den sonra `#closed` gibi bir durum da yazmayın: Taiga hikâyeyi otomatik
> kapatır, oysa hikâyeyi yalnızca PO kapatmalıdır.

**Dal adı:**

```text
<ekip>/TG-<numara>-<kısa-açıklama>
ekip3/TG-42-odunc-limit-kontrolu
```

**Commit mesajı:**

```text
<tür>: <kısa açıklama> (TG-<numara>)
ozellik: ogrenci odunc limiti kontrolu eklendi (TG-42)
```

| Tür | Kullanım |
|---|---|
| `ozellik` | Yeni özellik |
| `duzeltme` | Hata düzeltme |
| `test` | Yalnızca test ekleme veya değiştirme |
| `belge` | Yalnızca belge değişikliği |
| `yeniden` | Davranışı değiştirmeyen kod iyileştirmesi (refactoring) |

**PR başlığı:** `TG-42 Öğrenci ödünç limiti kontrolü`

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
