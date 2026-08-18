# Mulai dari Sini — Game Mini 15 Menit (sebelum Telur Wazan)

Sebelum membuka Telur Wazan yang besar, kita buat **game super sederhana dari nol**:
*seorang tokoh berjalan, mengumpulkan bintang, lalu MENANG.* Tanpa soal, tanpa peta acak.

Tujuannya: memahami **3 kata ajaib GDevelop** dengan tangan sendiri. Setelah ini, Telur
Wazan akan terasa seperti "game bintang ini, tapi diperbesar". Di tiap langkah ada kotak
**➜ Di Telur Wazan** yang menautkan apa yang baru kamu pelajari ke game aslinya.

> Cocok dikerjakan **bersama anak**. Aturan emas: **satu langkah → tekan Preview (▶) → lihat.**

---

## 3 kata ajaib

| Kata | Artinya untuk anak | Nanti di game bintang |
|---|---|---|
| **Scene** | panggung / layar | tempat kita bermain |
| **Objek** | pemain di panggung (gambar/tulisan) | Tokoh, Bintang, tulisan Skor |
| **Event** | aturan **JIKA … MAKA …** | JIKA sentuh bintang MAKA skor +1 |

Plus **Variabel** = kotak penyimpan angka (skor).

---

## Langkah 1 — Buat proyek & panggung

1. Buka GDevelop → **Create a new project** → **Empty game**.
2. Sudah ada satu **Scene** kosong. Klik dua kali untuk membukanya.

**➜ Di Telur Wazan:** ada **4 scene** (Menu, Hutan, Menang, Koleksi). Ini baru 1.

---

## Langkah 2 — Tokoh yang bisa berjalan (Objek + Behavior)

1. Di panggung: **Add a new object** → **Sprite** → beri satu gambar (apa saja, mis. kotak
   atau gambar anak) → namai **`Tokoh`** → **Apply**.
2. Letakkan Tokoh di panggung (drag).
3. Klik Tokoh → panel kanan **Behaviors** → **Add behavior** → **Top-down movement**.
4. **Preview (▶)** → tokohmu **sudah bisa jalan pakai panah**, tanpa menulis apa pun!

Itulah **Behavior**: perilaku siap pakai yang tinggal dipasang.

**➜ Di Telur Wazan:** objek `Petualang` juga memakai behavior **Top-down movement** yang
sama persis. Kamu baru saja membuat "petualang" versi mini.

> **Ajak anak:** "Gerakkan dia pakai panah!" Rasa "aku bisa menggerakkannya" adalah pemantik
> semangat pertama.

---

## Langkah 3 — Barang yang dikumpulkan (banyak Instance dari 1 Objek)

1. **Add a new object** → **Sprite** → gambar bintang/koin → namai **`Bintang`** → Apply.
2. Drag Bintang ke panggung. Lalu **salin–tempel** (Ctrl+C, Ctrl+V) beberapa kali → taruh 3
   bintang di tempat berbeda.

Kamu punya **1 Objek** `Bintang`, tapi **3 Instance** (salinan) di panggung.

**➜ Di Telur Wazan:** `Telur` juga satu objek, tapi disebar jadi banyak. Bedanya di Telur
Wazan penyebarannya dilakukan otomatis oleh event (peta acak) — idenya sama.

---

## Langkah 4 — Papan skor (Objek Teks + Variabel)

1. **Add a new object** → **Text** → isi `Skor: 0` → namai **`TeksSkor`** → Apply. Taruh di pojok.
2. Buat variabel skor: **Scene → Variables** (atau ikon variabel scene) → tambah variabel
   **`Skor`**, tipe angka, nilai **0**.

**➜ Di Telur Wazan:** ada variabel scene `Skor` dan teks `TeksSkor` yang persis begini
(tertulis `0 / 5`).

---

## Langkah 5 — Aturan pertama: JIKA sentuh bintang MAKA skor +1 (Event!)

Buka tab **Events** (di atas panggung) → **Add event**.

1. **Add condition** → pilih **`Tokoh`** → **Collision** → objek lain **`Bintang`**.
   (Artinya: *JIKA Tokoh menyentuh Bintang…*)
2. **Add action** → **`Bintang`** → **Delete** the object. (*…MAKA hapus bintang itu*)
3. **Add action** lagi → **Variables → Change number variable** → `Skor` → **+** `1`.
4. **Add action** lagi → **`TeksSkor`** → **Modify the text** → isi:
   `"Skor: " + ToString(Skor)`

**Preview.** Jalan ke bintang → bintang hilang, skor bertambah. 🎉 Kamu baru membuat
aturan **JIKA … MAKA …** pertamamu.

**➜ Di Telur Wazan:** aturan intinya sama — *JIKA `Petualang` collision `Telur` MAKA …* —
hanya saja "MAKA"-nya lebih ramai: telur pecah, muncul soal, dan seterusnya.

> **Ajak anak:** baca kerasnya. "**JIKA** tokoh kena bintang, **MAKA** bintang hilang dan
> skor tambah satu." Ini cara berpikir logis yang dipakai di semua pemrograman.

---

## Langkah 6 — Menang (JIKA skor cukup MAKA tampilkan tulisan)

1. **Add a new object** → **Text** → isi `MENANG!` → namai **`TeksMenang`** → Apply. Taruh di
   tengah, lalu **sembunyikan** dulu (klik kanan instance → *Hide*, atau atur lewat event).
2. Tab **Events** → **Add event**:
   - **Condition** → **Variables → Compare number variable** → `Skor` **≥** `3`.
   - **Action** → **`TeksMenang`** → **Show**.

**Preview.** Kumpulkan 3 bintang → muncul **MENANG!**

**➜ Di Telur Wazan:** ide "JIKA skor cukup MAKA menang" persis sama. Bedanya di sana kamu
juga harus **sampai ke FINISH** dulu, dan menangnya pindah ke scene `Menang`.

---

## Kamu sudah paham semuanya! Peta ke Telur Wazan

Game bintang tadi = Telur Wazan versi kecil. Yang kamu pelajari langsung berlaku:

| Di game bintang | Di Telur Wazan | Bagian tutorial |
|---|---|---|
| 1 scene | 4 scene (Menu, Hutan, Menang, Koleksi) | Bagian 2–3 |
| `Tokoh` + Top-down movement | `Petualang` (+ kepala terpisah) | Bagian 4 |
| 3 `Bintang` ditaruh tangan | banyak `Telur` disebar otomatis (peta acak) | Bagian 8 |
| Variabel `Skor`, `TeksSkor` | `Skor`, `TeksSkor` (`0 / 5`) | Bagian 6 |
| JIKA sentuh bintang MAKA skor+1 | JIKA sentuh telur MAKA telur pecah → soal | Bagian 5 & 7 |
| JIKA skor ≥ 3 MAKA MENANG | JIKA skor cukup **dan** sampai FINISH MAKA scene Menang | Bagian 7 |

**Konsep tambahan** yang membuat Telur Wazan lebih besar (dipelajari bertahap di `TUTORIAL.md`):

- **Mode permainan** (variabel `Status`: jalan → soal → hasil/salah) — seperti lampu lalu lintas.
- **Peta acak** yang dibuat oleh event (labirin otomatis, beda tiap main).
- **Suara** — di Telur Wazan **anak merekam suaranya sendiri**.
- **Menyimpan koleksi** boneka antar-sesi.

---

## Lanjut ke sini

➡️ Buka **`TUTORIAL.md`** dan mulai dari **Bagian 0** (buka `game.json`, tekan Preview).
Semua yang barusan kamu bangun akan kamu temui lagi di sana — tinggal lebih besar.

> **Untuk mengajar anak:** ulangi pola ini setiap kali — *satu perubahan kecil → Preview →
> "apa yang berubah?"*. Rayakan kalau ada yang rusak; itu justru momen belajar terbaik.
