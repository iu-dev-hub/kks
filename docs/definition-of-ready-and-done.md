# Definition of Ready and Definition of Done

## Hazır Tanımı (Definition of Ready)

Bir iş sprinte alınmadan önce:

- [ ] Kullanıcı hikâyesi formatında yazılmış
- [ ] Kabul kriterleri Given / When / Then formatında belirlenmiş
- [ ] Sınır durumlar kabul kriterlerinde yer alıyor
- [ ] Diğer ekiplere bağımlılıklar belirtilmiş
- [ ] Ekip tarafından tahminlenmiş (Taiga'da story point girilmiş)
- [ ] Bir sprintte bitirilebilecek büyüklükte (8 puandan büyükse bölünmeli)

## Bitti Tanımı (Definition of Done)

Bir iş "bitti" sayılmadan önce:

- [ ] Kod yazılmış, PR açılmış ve en az bir kişi tarafından incelenmiş
- [ ] Yeni kod için birim testleri yazılmış
- [ ] Her kabul kriteri için en az bir otomatik test var (entegrasyon veya E2E)
- [ ] CI yeşil (ruff, birim, entegrasyon, E2E)
- [ ] Arayüz sözleşmesi etkilendiyse güncellenmiş
- [ ] Testçi kabul kriterlerini doğrulamış
- [ ] Hikâyenin Taiga görevleri kapatılmış
- [ ] Product Owner hikâyeyi Taiga'da **Bitti**'ye taşımış
