[English](Step-2-Domain-Storage) · [Dansk](Step-2-Domain-Storage-da) · **Bahasa Malaysia**

# Langkah 2: Domain dan storan

![Langkah 2: papan dibaca daripada SQLite](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-02.png)

## Apa yang kita bina

Peraturan teras papan dan storannya. Halaman kini membaca papan daripada fail SQLite dan memaparkan lima senarai lalai bersama kadnya.

## Model domain

| Konsep | Medan | Peraturan |
| --- | --- | --- |
| Papan | id, nama | Storan baharu mendapat satu papan dengan senarai Backlog, To Do, In Progress, Review dan Done |
| Senarai | id, papan, nama, kedudukan | Senarai disusun dari kiri ke kanan; kedudukan tiada jurang |
| Kad | id, senarai, tajuk, kedudukan | Kad disusun dari atas ke bawah; satu kad berada dalam tepat satu senarai |

Kes guna: dapatkan papan, cipta, namakan semula, padam dan alih senarai, serta cipta, namakan semula, padam dan alih kad. Nama dipangkas, tidak boleh kosong dan paling banyak 100 aksara.

## Apa yang kita perolehi

- **Entiti.** Kelas data kecil yang tidak berubah (`Board`, `CardList`, `Card`) menyimpan data; kelas senarai dinamakan `CardList` kerana `list` ialah binaan dalam Python.
- **Satu port.** `BoardRepository` ialah `Protocol` dalam domain; aplikasi bergantung padanya, bukan pada SQLite.
- **Kelas kes guna.** Satu kelas kecil bagi setiap tindakan dengan satu kaedah `execute`.
- **Satu penyesuai.** `SqliteBoardRepository` melaksanakan port dengan modul standard `sqlite3`, pertanyaan berparameter dan satu transaksi bagi setiap panggilan.
- **Dua jenis ujian.** Ujian unit menggunakan tiruan dalam memori; ujian integrasi menjalankan penyesuai sebenar pada fail sementara. Liputan ialah 99 peratus.
- **Kedudukan tanpa jurang.** Mengalih atau memadam menomborkan semula jiran dalam transaksi yang sama.
