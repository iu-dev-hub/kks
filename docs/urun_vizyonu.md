# Ürün Vizyonu: Kampüs Kütüphane Sistemi

**Kimin için?** Üniversitedeki öğrenciler, akademisyenler ve kütüphane görevlileri

**Sorun ne?** Kütüphanedeki ödünç işlemleri kâğıt formlar ve tablolarla yürütülüyor.
Kullanıcılar hangi kitabın rafta olduğunu bilmiyor, geciken iadeler takip edilemiyor.

**Ürün ne yapacak?**

- Kullanıcılar kayıt olup giriş yapabilecek.
- Katalogda kitap arayıp durumunu (rafta, ödünçte, rezerveli) görebilecek.
- Kitap ödünç alıp iade edebilecek, süre uzatabilecek, rezervasyon yapabilecek.
- Geciken iadeler için ceza otomatik hesaplanacak, kullanıcı bilgilendirilecek.
- Görevliler istatistik ve raporları görüntüleyebilecek.

**Başarıyı nasıl ölçeceğiz?**

- Temel akış (kayıt → giriş → arama → ödünç → iade) hatasız çalışıyor.
- Tüm iş kuralları otomatik testlerle doğrulanmış.
- Dönem sonunda v1.0 sürümü, yeşil CI ile yayına hazır.

**Kapsam dışı (bu dönem):** Mobil uygulama, e-kitap, ödeme entegrasyonu, e-posta gönderimi
(bildirimler sistem içinde gösterilir).
