[English](Step-6-Wrap-Up) · [Dansk](Step-6-Wrap-Up-da) · **Bahasa Malaysia**

# Langkah 6: Penutup dan refleksi

![Langkah 6: papan yang siap](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-06.png)

## Apa yang kita bina

Langkah terakhir tidak menambah ciri. Ia menyemak bahawa keseluruhan projek berfungsi untuk orang yang dituju: peserta kursus yang mengklon projek, mencipta `.venv`, menjalankan ujian dan memulakan papan, dan pelawat yang hanya membaca huraian, README dan wiki ini. Semakan kualiti penuh (ujian, liputan, ujian pelayar dalam kontena, dokumentasi sumber, imbasan kod dan semakan rangka kerja) dijalankan pada kod akhir.

## Apa yang kita peroleh

- **Projek yang boleh diserahkan.** Persediaan dalam README diikuti secara literal dalam kontena yang bersih.
- **Satu set halaman dalam tiga bahasa** dengan bar sisi dan baris bahasa pada setiap halaman.
- **Refleksi** (di bawah) yang menyebut apa yang mudah, apa yang sukar dan apa yang akan kita ubah.

## Refleksi

- **Pendekatan.** Rancang dahulu: kes perniagaan, pihak berkepentingan, pelan projek dan enam pencapaian diluluskan sebelum baris kod pertama. Setiap pencapaian ialah satu cabang, satu semakan dan satu pull request, dan setiap langkah menghasilkan tangkapan skrin dan halaman wiki.
- **Yang mudah.** Peraturan domain dan SQLite. Papan, senarai dan kad ialah model kecil, dan lapisan memastikan peraturan bebas daripada HTTP dan SQL, jadi kebanyakan ujian berjalan dalam milisaat terhadap stor dalam memori.
- **Yang sukar.** Seret lepas. Peristiwa pelayar bersifat aras rendah: kedudukan lepas mesti dikira daripada penuding, dan ujian mesti menyeret dalam pelayar sebenar. Tarikh juga lebih sukar daripada dijangka, kerana penghurai yang longgar menerima bentuk yang tidak dikehendaki.
- **Pembelajaran terbesar.** Rangka kerja ialah pilihan yang ada kosnya. Pustaka standard (`http.server`, `sqlite3`) sudah mencukupi, jadi projek tiada kebergantungan semasa larian dan pembaca melihat setiap lapisan. Rangka kerja web akan menjimatkan kod penghalaan, tetapi turut menyembunyikan pengajarannya.
- **Apa yang akan dibuat secara berbeza.** Memulakan ujian pelayar lebih awal, memberi penghala jadual ujian kecil sejak hari pertama, dan memilih teknologi bersama pengguna sebelum pencapaian pertama, supaya perubahan fikiran lewat tidak membawa kos.
