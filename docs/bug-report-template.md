# Bug Report Template (Taiga)

Taiga'da **Issues → New issue** ekranında tür olarak **Bug** seçin, önem derecesini
belirleyin, ekip etiketini (`team-membership` vb.) ekleyin ve aşağıdaki şablonu açıklama alanına yapıştırıp doldurun.

```markdown
**İlgili hikâye:** #
**Modül / Ekip:** (Membership / Catalog / Loans / Fines-Reports)

**Ortam:** (Tarayıcı ve sürümü, dal adı, commit)

**Ön koşullar:** (Kullanıcı rolü, test verisi)

**Adımlar:**
1.
2.
3.

**Beklenen sonuç:**

**Gerçekleşen sonuç:**

**Nasıl bulundu?** (Otomatik test / Test tasarım tekniği / Keşif testi / Çapraz test / Kod incelemesi)

**Ekler:** (GitHub'daki "Hata Ekleri" kaydının veya CI çalıştırmasının bağlantısı)
```

## İyi bir hata raporunun özellikleri

- **Tekrar oluşturulabilir:** Geliştirici adımları izleyince aynı hatayı görmeli.
- **Tek bir hata:** İki farklı sorun varsa iki ayrı kayıt açın.
- **Nesnel:** "Çok kötü çalışıyor" değil, "3. kitapta uyarı çıkmıyor".
- **Önem derecesi ile öncelik ayrı:** Önem derecesini testçi, önceliği PO belirler.

**Örnek başlık:** `Öğrenci 3 kitabı ödünçteyken 4. kitabı ödünç alabiliyor`
