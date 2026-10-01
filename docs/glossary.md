# Glossary (Terimler Sözlüğü)

Kodda İngilizce, arayüzde ve belgelerde Türkçe kullandığımız terimler.
Yeni bir terim kullanmaya başladığınızda buraya ekleyin (PR ile).

## Alan (domain) terimleri

| Kodda (English) | Türkçe | Örnek kullanım |
|---|---|---|
| `user` | kullanıcı | `users` tablosu |
| `member`, `membership` | üye, üyelik | `app/membership/` |
| `student` | öğrenci | `role = "student"` |
| `academic` | akademisyen | `role = "academic"` |
| `librarian` | kütüphane görevlisi | `role = "librarian"` |
| `book` | kitap | `books` tablosu |
| `catalog` | katalog | `app/catalog/` |
| `isbn` | ISBN | `books.isbn` |
| `title` / `author` | başlık / yazar | `books.title` |
| `loan` | ödünç (işlemi) | `loans` tablosu |
| `borrow` | ödünç almak | `can_borrow()` |
| `return` | iade etmek | `return_book()` |
| `due_date` | son iade tarihi | `loans.due_date` |
| `borrowed_at` / `returned_at` | alış / iade tarihi | `loans.returned_at` |
| `overdue` | gecikmiş | `days_overdue()` |
| `renew`, `renewal` | süre uzatmak, uzatma | `renew_loan()` |
| `reservation`, `reserve` | rezervasyon, rezerve etmek | `reserve_book()` |
| `on_shelf` | rafta | `books.status` |
| `on_loan` | ödünçte | `books.status` |
| `fine` | ceza | `fines` tablosu |
| `fine cap` | ceza tavanı | `MAX_FINE = 50` |
| `paid` | ödendi | `fines.paid` |
| `report` | rapor | `app/fines_reports/` |
| `limit` | limit, üst sınır | `MAX_LOANS_STUDENT = 3` |

## Süreç ve test terimleri

| English | Türkçe |
|---|---|
| backlog / product backlog | ürün iş listesi |
| user story | kullanıcı hikâyesi |
| acceptance criteria | kabul kriterleri |
| definition of ready / done | hazır tanımı / bitti tanımı |
| sprint / increment | sprint / artım |
| refinement | backlog iyileştirme |
| retrospective | retrospektif |
| impediment | engel |
| pull request (PR) | birleştirme isteği |
| code review | kod incelemesi |
| continuous integration (CI) | sürekli entegrasyon |
| test case | test durumu |
| test suite | test paketi |
| regression testing | regresyon testi |
| smoke test | duman testi |
| unit / integration / end-to-end (E2E) test | birim / entegrasyon / uçtan uca test |
| equivalence partitioning | denklik sınıfı bölümleme |
| boundary value analysis | sınır değer analizi |
| decision table testing | karar tablosu testi |
| state transition testing | durum geçiş testi |
| statement / branch coverage | komut / karar (dal) kapsamı |
| exploratory testing | keşif testi |
| error / defect / failure | hata / kusur / arıza |
| root cause | kök neden |
| severity / priority | önem derecesi / öncelik |
| testability | test edilebilirlik |
| mock / stub | sahte nesne / taslak |
| fixture | (pytest) test hazırlığı |
