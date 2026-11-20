[English](Step-5-Card-Details) · [Dansk](Step-5-Card-Details-da) · **Bahasa Malaysia**

# Langkah 5: Butiran kad

![Langkah 5: dialog butiran kad](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-05.png)

## Apa yang kita bina

Kad kini lebih daripada tajuk. Klik pada kad untuk membuka dialog di mana anda menetapkan label berwarna, huraian, tarikh akhir dan status selesai, serta menambah atau memadam komen teks. Pada papan, setiap kad menunjukkan jalur label, ikon huraian, bilangan komen dan lencana tarikh akhir. Kad yang lewat mempunyai lencana tarikh merah dan kad yang selesai dipalang.

## Apa yang kita peroleh

- **Pemodelan data.** Kad mendapat lima maklumat baru: label, huraian, tarikh akhir, selesai dan komen. Komen ialah jadual sendiri dengan kunci asing dan `ON DELETE CASCADE`, jadi memadam kad turut membuang komennya.
- **Pengesahan di satu tempat.** Peraturan untuk label (palet tetap), panjang huraian dan komen, serta tarikh akhir berada dalam `domain/detail_rules.py`. Nilai yang salah menimbulkan ralat domain dan penghala menjawab 400.
- **Tarikh.** Tarikh akhir ialah rentetan `TTTT-BB-HH`. `datetime.date.fromisoformat` terlalu longgar, jadi peraturan turut menyemak bentuknya; 2026-02-30 ditolak. Pelayar menentukan lewat dengan membandingkan rentetan itu dengan tarikh hari ini.
- **Migrasi.** Apabila pangkalan data dari langkah terdahulu dibuka, lajur baru dan jadual komen ditambah dan `PRAGMA user_version` ditetapkan, jadi tiada data hilang.
- **Kemas kini separa.** `PATCH /api/cards/{id}` hanya mengubah medan yang dihantar; `due_date: null` mengosongkan tarikh.
- **Dialog asli.** Elemen `dialog` memberi pengurusan fokus, Escape untuk menutup dan latar belakang tanpa pustaka.
