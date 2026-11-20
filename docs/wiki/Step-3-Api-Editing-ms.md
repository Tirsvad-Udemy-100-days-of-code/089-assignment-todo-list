[English](Step-3-Api-Editing) · [Dansk](Step-3-Api-Editing-da) · **Bahasa Malaysia**

# Langkah 3: API JSON dan penyuntingan

![Langkah 3: senarai baharu dan borang kad](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-03.png)

## Apa yang kita bina

API JSON untuk senarai dan kad serta halaman yang menggunakannya: anda boleh menambah, menamakan semula dan memadam senarai dan kad tanpa memuat semula halaman. Pelayan hanya menghantar kerangka HTML kecil; JavaScript biasa membina papan.

## API

| Kaedah dan laluan | Fungsi | Berjaya |
| --- | --- | --- |
| `GET /api/board` | Papan dengan senarai dan kad | 200 |
| `POST /api/lists` | Tambah senarai (`board_id`, `name`) | 201 |
| `PATCH /api/lists/{id}` | Namakan semula senarai | 200 |
| `DELETE /api/lists/{id}` | Padam senarai dan kadnya | 204 |
| `POST /api/lists/{id}/cards` | Tambah kad (`title`) | 201 |
| `PATCH /api/cards/{id}` | Namakan semula kad | 200 |
| `DELETE /api/cards/{id}` | Padam kad | 204 |

Ralat ialah JSON dengan mesej `error`: 400 untuk nama atau kandungan yang tidak sah, 404 untuk id atau laluan yang tidak dikenali, 405 untuk kaedah yang salah. Jejak tindanan tidak pernah dihantar.

## Apa yang kita perolehi

- **Penghala kecil.** Laluan memetakan kaedah dan corak laluan (`{id}`) kepada fungsi pengawal; satu tempat menukar ralat domain kepada kod status.
- **HTTP dalam Python biasa.** `http.server` membaca kandungan dan menulis jawapan; pengawal tidak pernah melihat soket.
- **Pengesahan di pinggir.** `require_str` dan `require_int` menyemak setiap medan JSON sebelum kes guna berjalan.
- **Halaman tanpa rangka kerja.** `app.js` menggunakan `fetch`, membina DOM dengan `textContent` (supaya nama tidak boleh menyuntik HTML) dan melukis semula selepas setiap perubahan.
- **Ujian pelayar tanpa desktop.** Ujian hujung-ke-hujung berjalan dalam bekas Docker dengan pelayar tanpa skrin dan menulis hasil ke fail.
