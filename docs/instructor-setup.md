# Instructor Setup (Öğretim Üyesi Kurulum Rehberi)

Tahmini süre: 3–4 saat (GitHub + Taiga). Adımları sırayla izleyin.

## 1. GitHub organizasyonu

1. GitHub'da **New organization → Free** planla bir organizasyon oluşturun (ör. `iu-dev-hub`).
2. Ücretsiz planda dal koruma kuralları yalnızca **public** depolarda çalışır.
   İki seçenek:
   - Depoyu **public** yapın (en kolayı), **veya**
   - GitHub Education'a öğretim üyesi olarak başvurun; onaylandıktan sonra
     organizasyonu GitHub Education panelinden ücretsiz **GitHub Team** planına yükseltin.
     (Organizasyonu Team planla değil, Free planla oluşturup sonra yükseltin.)

## 2. Depo

1. Organizasyonda `kks` adında boş bir depo oluşturun.
2. Bu iskeleti depoya yükleyin:

```bash
cd kks
git init -b main
git add .
git commit -m "chore: initial project skeleton"
git remote add origin https://github.com/iu-dev-hub/kks.git
git push -u origin main
```

3. Actions sekmesinde CI'ın yeşil olduğunu doğrulayın.
4. `.github/CODEOWNERS` dosyasındaki öğretim üyesi kullanıcı adının (`@imyo-dev-hub`)
   GitHub kullanıcı adınızla aynı olduğunu kontrol edin.

## 3. Takımlar

Organizasyon → **Teams** → aşağıdaki takımları **Visible** olarak oluşturun:

`team-membership`, `team-catalog`, `team-loans`, `team-fines-reports`,
`product-owners`, `scrum-masters`, `developers`, `qa`

Öğrencileri davet edin (Organizasyon → People → Invite) ve takımlara ekleyin.
Her öğrenci bir ekip takımında ve bir rol takımında olur. Back ve Front geliştiriciler
`developers`, testçiler `qa` takımına girer.

## 4. Depo yetkileri

Depo → Settings → **Collaborators and teams**: Tüm takımlara **Write** yetkisi verin.
(CODEOWNERS'taki takımların Write yetkisi olmazsa onay veremezler.)

## 5. Dal koruma (Ruleset)

Depo → Settings → **Rules → Rulesets → New branch ruleset**

- Ad: `main-koruma`, Enforcement: **Active**, Target: **Default branch**
- Bypass list: **Organization admin** rolü (eksik üye ve acil durumlar için)
- Açılacak kurallar:
  - **Restrict deletions**
  - **Block force pushes**
  - **Require a pull request before merging**
    - Required approvals: **1**
    - **Dismiss stale pull request approvals when new commits are pushed**
    - **Require review from Code Owners**
  - **Require status checks to pass**
    - Ekleyin: `Lint (ruff)`, `Unit and integration tests`, `E2E tests (Playwright)`
      (Bu adlar listede yalnızca CI en az bir kez çalıştıktan sonra görünür.)
    - **Require branches to be up to date before merging**

## 6. Taiga

`docs/project-management.md` dosyasındaki Bölüm 1 (Taiga projesi) ve Bölüm 2
(Taiga–GitHub bağlantısı) adımlarını uygulayın. Webhook'u kurduktan sonra boş bir
commit ile bağlantıyı mutlaka test edin.

## 7. Discussions

Depo → Settings → Features → **Discussions**'ı açın. Kategoriler:

- `Günlük` (her ekip için sabitlenmiş bir başlık)
- `Scrum of Scrums` (Entegrasyon kararları)
- `Soru-Cevap`
- `Duyurular` (yalnızca öğretim üyesi)

## 8. İlk ürün backlog'u

Dönem başlamadan Taiga'da her modül için bir **Epic** ve 3–5 başlangıç hikâyesi yazın.
İlk sprintte PO'lar bunları örnek alarak kendi hikâyelerini yazar.

## Eksik üye olduğunda

Yedek yoktur; boş kalan rolü siz üstlenirsiniz (karar, onay, kod incelemesi, kabul testi).
GitHub'da CODEOWNERS onayı gerekiyorsa admin olarak onay verebilir veya dal kuralını
o PR için atlayabilirsiniz (bypass). Taiga'da admin olduğunuz için ek ayar gerekmez.

## Her rol döneminin sonunda (Hafta 5, 9, 13)

1. Rol takımlarının üyelerini güncelleyin (ekip takımlarına dokunmayın).
2. `ROLES.md`'yi PR ile güncelleyin.
3. Taiga'da öğrencilerin rollerini değiştirin (Settings → Members).
