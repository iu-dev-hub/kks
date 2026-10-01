# İş Kuralları (Sürüm 1.0)

> Bu belge müşteri (Baş Product Owner) tarafından yönetilir. Dönem içinde
> **değişebilir**. Her değişiklik sürüm numarasıyla birlikte aşağıdaki
> "Değişiklik geçmişi" bölümüne yazılır.

## K1. Kullanıcılar ve roller (Ekip 1)

- K1.1 Roller: öğrenci, akademisyen, görevli
- K1.2 E-posta adresi benzersiz olmalıdır.
- K1.3 Şifre 8–20 karakter olmalı, en az bir harf ve bir rakam içermelidir.
- K1.4 Üst üste 3 hatalı girişten sonra hesap 15 dakika kilitlenir.

## K2. Katalog (Ekip 2)

- K2.1 Her kitabın benzersiz bir ISBN'i vardır (10 veya 13 haneli).
- K2.2 Arama; başlık, yazar veya ISBN ile yapılabilir. Arama metni en az 2 karakterdir.
- K2.3 Kitap ekleme, düzenleme ve silme işlemlerini yalnızca görevliler yapabilir.
- K2.4 Ödünçte olan bir kitap silinemez.

## K3. Ödünç alma (Ekip 3)

| Kural | Öğrenci | Akademisyen |
|---|---|---|
| K3.1 Aynı anda en fazla ödünç kitap | 3 | 10 |
| K3.2 Ödünç süresi | 14 gün | 30 gün |
| K3.3 Süre uzatma hakkı | 1 kez | 2 kez |

- K3.4 Her uzatma, süreyi kullanıcının ödünç süresi kadar uzatır.
- K3.5 Ödenmemiş cezası olan kullanıcı yeni kitap ödünç alamaz ve süre uzatamaz.
- K3.6 Başka bir kullanıcı tarafından rezerve edilmiş kitabın süresi uzatılamaz.
- K3.7 Bir kullanıcı aynı anda en fazla 2 rezervasyon yapabilir.
- K3.8 Rezerve edilen kitap iade edildiğinde 3 gün boyunca yalnızca rezerve eden kişi alabilir.

## K4. Ceza ve rapor (Ekip 4)

- K4.1 Gecikme cezası günlük **2 TL**'dir.
- K4.2 Bir ödünç işlemi için ceza en fazla **50 TL** olabilir.
- K4.3 Son gün yapılan iade gecikme sayılmaz.
- K4.4 Görevli, ödünç istatistiklerini (en çok ödünç alınan kitaplar, geciken iadeler) görebilir.

## Kitap durumları

```text
Rafta     --ödünç verilir-->        Ödünçte
Ödünçte   --zamanında iade-->       Rafta
Ödünçte   --süre dolar-->           Gecikmiş
Gecikmiş  --iade (ceza oluşur)-->   Rafta
Rafta     --rezerve edilir-->       Rezerveli
Ödünçte   --başkası rezerve eder--> Ödünçte (rezerveli)
Rezerveli --rezerve eden alır-->    Ödünçte
```

## Değişiklik geçmişi

| Sürüm | Tarih | Değişiklik |
|---|---|---|
| 1.0 | | İlk sürüm |
