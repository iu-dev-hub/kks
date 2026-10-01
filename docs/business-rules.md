# Business Rules (İş Kuralları) — Sürüm 1.0

> Bu belge müşteri (Baş Product Owner) tarafından yönetilir. Dönem içinde
> **değişebilir**. Her değişiklik sürüm numarasıyla birlikte aşağıdaki
> "Değişiklik geçmişi" bölümüne yazılır.

## BR-1. Kullanıcılar ve roller (Team Membership)

- BR-1.1 Roller: öğrenci (`student`), akademisyen (`academic`), görevli (`librarian`)
- BR-1.2 E-posta adresi benzersiz olmalıdır.
- BR-1.3 Şifre 8–20 karakter olmalı, en az bir harf ve bir rakam içermelidir.
- BR-1.4 Üst üste 3 hatalı girişten sonra hesap 15 dakika kilitlenir.

## BR-2. Katalog (Team Catalog)

- BR-2.1 Her kitabın benzersiz bir ISBN'i vardır (10 veya 13 haneli).
- BR-2.2 Arama; başlık, yazar veya ISBN ile yapılabilir. Arama metni en az 2 karakterdir.
- BR-2.3 Kitap ekleme, düzenleme ve silme işlemlerini yalnızca görevliler yapabilir.
- BR-2.4 Ödünçte olan bir kitap silinemez.

## BR-3. Ödünç alma (Team Loans)

| Kural | Öğrenci | Akademisyen |
|---|---|---|
| BR-3.1 Aynı anda en fazla ödünç kitap | 3 | 10 |
| BR-3.2 Ödünç süresi | 14 gün | 30 gün |
| BR-3.3 Süre uzatma hakkı | 1 kez | 2 kez |

- BR-3.4 Her uzatma, süreyi kullanıcının ödünç süresi kadar uzatır.
- BR-3.5 Ödenmemiş cezası olan kullanıcı yeni kitap ödünç alamaz ve süre uzatamaz.
- BR-3.6 Başka bir kullanıcı tarafından rezerve edilmiş kitabın süresi uzatılamaz.
- BR-3.7 Bir kullanıcı aynı anda en fazla 2 rezervasyon yapabilir.
- BR-3.8 Rezerve edilen kitap iade edildiğinde 3 gün boyunca yalnızca rezerve eden kişi alabilir.

## BR-4. Ceza ve rapor (Team Fines-Reports)

- BR-4.1 Gecikme cezası günlük **2 TL**'dir.
- BR-4.2 Bir ödünç işlemi için ceza en fazla **50 TL** olabilir.
- BR-4.3 Son gün yapılan iade gecikme sayılmaz.
- BR-4.4 Görevli, ödünç istatistiklerini (en çok ödünç alınan kitaplar, geciken iadeler) görebilir.

## Kitap durumları (`books.status`)

| Kod değeri | Arayüzde |
|---|---|
| `on_shelf` | Rafta |
| `on_loan` | Ödünçte |
| `overdue` | Gecikmiş |
| `reserved` | Rezerveli |

```text
on_shelf  --ödünç verilir-->        on_loan
on_loan   --zamanında iade-->       on_shelf
on_loan   --süre dolar-->           overdue
overdue   --iade (ceza oluşur)-->   on_shelf
on_shelf  --rezerve edilir-->       reserved
on_loan   --başkası rezerve eder--> on_loan (rezerveli)
reserved  --rezerve eden alır-->    on_loan
```

## Değişiklik geçmişi

| Sürüm | Tarih | Değişiklik |
|---|---|---|
| 1.0 | | İlk sürüm |
