-- Kampüs Kütüphane Sistemi: Başlangıç şeması
--
-- Bu şema bir BAŞLANGIÇ noktasıdır. Ekipler Sprint 2'de arayüz sözleşmesini
-- (docs/arayuz_sozlesmesi.md) yaparken tabloları birlikte genişletecektir.
-- Bir tabloya sütun eklemek diğer ekipleri etkileyebilir: önce konuşun!

DROP TABLE IF EXISTS ceza;
DROP TABLE IF EXISTS odunc;
DROP TABLE IF EXISTS kitap;
DROP TABLE IF EXISTS kullanici;

-- Sahibi: Ekip 1 (Üyelik)
CREATE TABLE kullanici (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    eposta      TEXT    NOT NULL UNIQUE,
    sifre_ozeti TEXT    NOT NULL,
    ad_soyad    TEXT    NOT NULL,
    rol         TEXT    NOT NULL CHECK (rol IN ('ogrenci', 'akademisyen', 'gorevli'))
);

-- Sahibi: Ekip 2 (Katalog)
CREATE TABLE kitap (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn    TEXT    NOT NULL UNIQUE,
    baslik  TEXT    NOT NULL,
    yazar   TEXT    NOT NULL,
    durum   TEXT    NOT NULL DEFAULT 'rafta'
);

-- Sahibi: Ekip 3 (Ödünç)
CREATE TABLE odunc (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_id  INTEGER NOT NULL REFERENCES kullanici (id),
    kitap_id      INTEGER NOT NULL REFERENCES kitap (id),
    alis_tarihi   TEXT    NOT NULL,
    son_tarih     TEXT    NOT NULL,
    iade_tarihi   TEXT
);

-- Sahibi: Ekip 4 (Ceza ve Rapor)
CREATE TABLE ceza (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    odunc_id  INTEGER NOT NULL REFERENCES odunc (id),
    tutar     INTEGER NOT NULL,
    odendi    INTEGER NOT NULL DEFAULT 0
);
