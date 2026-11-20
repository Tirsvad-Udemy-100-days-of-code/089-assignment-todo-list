[English](Step-4-Kanban-Board) · [Dansk](Step-4-Kanban-Board-da) · **Bahasa Malaysia**

# Langkah 4: Papan Kanban dan seret lepas

![Langkah 4: kad diseret dari To Do ke Review](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-04.png)

## Apa yang kita bina

Papan kini berfungsi seperti papan Kanban. Kad bergerak antara senarai dan dalam satu senarai, dan senarai bergerak ke kiri dan kanan, semuanya dengan seret lepas. Setiap pergerakan disimpan: selepas muat semula, papan kelihatan sama.

Lakaran yang membimbing rupa papan (latar biru, lajur senarai bulat, kad putih, kawalan Add a card di bawah setiap senarai):

![Lakaran papan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/wireframes/board.svg)

## Apa yang kita perolehi

- **Dua titik akhir alih.** `PATCH /api/cards/{id}/move` menerima `list_id` dan `position`; `PATCH /api/lists/{id}/move` menerima `position`. Storan menomborkan semula jiran dalam satu transaksi, jadi kedudukan tiada jurang dan kedudukan melepasi hujung bermaksud hujung.
- **Seret lepas asli.** Peristiwa pelayar `dragstart`, `dragover` dan `drop` mencukupi. Kedudukan ialah bilangan kad yang tengahnya berada di atas penuding.
- **Maklum balas visual.** Kad yang diseret menjadi pudar, dan senarai di bawah penuding mendapat garis putus-putus.
- **Reka letak responsif.** Papan boleh digulung ke sisi pada skrin sempit, dan senarai tidak pernah lebih lebar daripada skrin.
- **Ujian pelayar untuk seret.** Ujian dalam bekas Docker menyeret kad dan senarai serta menyemak susunan selepas muat semula.
