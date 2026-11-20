[English](Step-1-Foundation) · [Dansk](Step-1-Foundation-da) · **Bahasa Malaysia**

# Langkah 1: Asas projek

![Langkah 1: halaman pertama dengan lima senarai kosong](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-01.png)

## Apa yang kita bina

Projek Python yang telah dikonfigurasi dan memaparkan halaman pertama: papan biru dengan lima senarai kosong bernama Backlog, To Do, In Progress, Review dan Done.

## Apa yang kita perolehi

- **Persekitaran maya tempatan.** `python -m venv .venv` mengasingkan pakej projek daripada Python sistem, dan `python -m pip install --upgrade pip` memastikan pip terkini.
- **Satu fail projek.** `pyproject.toml` menyimpan versi Python (3.13 atau lebih baharu), senarai kebergantungan runtime yang kosong dan tetapan pytest, ruff dan mypy.
- **Pemalar di satu tempat.** `constants.py` menyimpan semua nilai tetap, jadi perubahan dibuat sekali sahaja.
- **Lapisan.** `domain`, `application`, `infrastructure` dan `presentation` mengasingkan peraturan daripada pangkalan data dan web; import menuju ke dalam.
- **MVC untuk web.** Pengawal menjawab permintaan dan paparan membina HTML.
- **Ujian dahulu.** pytest menjalankan ujian unit bagi paparan dan ujian integrasi bagi pelayan sebenar pada port bebas.
- **Dokumentasi daripada kod sumber.** Komen Doxygen dan `Doxyfile` membina dokumentasi kod.
- **Tangkapan skrin yang selamat.** Bekas Docker dengan pelayar tanpa skrin mengambil gambar, jadi desktop tidak pernah digunakan.
- **Imbasan sebelum setiap push.** opengrep menyemak kod dengan peraturan tempatan.
