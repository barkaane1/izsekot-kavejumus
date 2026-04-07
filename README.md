# 📊 Stundu kavējumu uzskaites sistēma

## 📝 Apraksts
Šī lietotne palīdz skolēniem sekot līdzi savam mācību apmeklējumam un automātiski aprēķināt kavējumu procentuālo vērtību. [cite_start]Tā nodrošina drošu datu glabāšanu SQLite datubāzē un iespēju labot profilu vai apskatīt vēsturi.

## 🛠 Tehnoloģijas
* **Backend:** Python (Flask ietvars)
* **Frontend:** HTML, CSS (pielāgoti fonti un responsīvs dizains )
* **Datubāze:** SQLite
* **Licence:** MIT

## 📐 Plānošana un Struktūra

### 1. Lietotāja saskarnes skices (Wireframes)
Lietotne ir izstrādāta, lai būtu lietojama gan uz datora, gan mobilajām ierīcēm.
>https://drive.google.com/file/d/1zzvATNpDV7Iw_PPNaTNWcslxxQIqf-4Y/view?usp=sharing

### 2. Datubāzes shēma (ERD)
Sistēma izmanto relāciju datubāzi ar trim galvenajām tabulām: `LIETOTAJI`, `KAVEJUMI` un `JAUNUMI`, nodrošinot 1:N saiti starp lietotāju un viņa ierakstiem.
>https://lucid.app/lucidchart/4912fda4-4571-478b-90e9-97a305ddc929/edit?viewport_loc=-641%2C441%2C1663%2C753%2C0_0&invitationId=inv_46e0b86a-2336-464c-a260-634a785a2874

## 📋 Prasību izpilde
* **Ātrdarbība:** Informācija ielādējas mazāk nekā 1500 ms.
***Drošība:** Datu aizsardzībai paredzēta SSL šifrēšana un unikāli lietotājvārdi.
* **Validācija:** Sistēma pieņem tikai skaitliskas vērtības stundu laukos.

## ⚖️ Licence
Šis projekts ir licencēts saskaņā ar **MIT licenci** – tas ir atvērts pirmkods, kuru drīkst brīvi lietot un mainīt.


