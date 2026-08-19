# Panduan Mengajar — Alur Tutoring untuk Anak (usia 8, 10, 12)

Cara **step-by-step** mengajarkan GDevelop lewat game ini, disesuaikan untuk tiga usia
sekaligus. Dipakai bersama:
- **`MULAI-DARI-SINI.md`** — kursus Level 0–4 (bikin "Telur Wazan mini" dari nol).
- **`TUTORIAL.md`** — membedah Telur Wazan yang asli.

> Karena kamu punya anak 8, 10, dan 12 sekaligus, panduan ini mengutamakan **mengajar bareng
> satu proyek dengan pembagian peran** (Mode A), lalu memberi jalur **sendiri-sendiri** (Mode B)
> untuk yang ingin lebih cepat.

---

## 0. Lima prinsip mengajar (berlaku semua usia)

1. **Satu perubahan → tekan Preview → "apa yang berubah?"** Ini ritme belajarnya.
2. **Baca event keras-keras** sebelum mengeklik: *"JIKA apa? MAKA apa? ada sarang tidak?"*
3. **Rayakan error.** Layar rusak = momen belajar terbaik: "aturan tadi bilang apa?"
4. **Anak harus merasa memiliki.** Beri mereka menggambar aset & merekam suara sesegera mungkin.
5. **Sesi pendek.** 8 th: 20–30 menit. 10 th: 30–40. 12 th: 40–50. Berhenti saat masih seru.

---

## 1. Apa yang realistis dipahami tiap usia

Gunakan sebagai *ekspektasi*, bukan batas mati — anak bisa melampaui.

| Konsep | 8 tahun | 10 tahun | 12 tahun |
|---|---|---|---|
| Scene, Objek, main game | Paham & lancar | Paham | Paham |
| Menggambar aset & rekam suara | **Andalan mereka** | Suka | Bisa, mungkin bosan |
| JIKA … MAKA … (baca) | Bisa **membaca**/mengucap | Membaca & menulis 1 event | Menulis & menjelaskan |
| DAN / TIDAK (Invert) | Dengan bantuan | Paham | Lancar |
| Variabel (angka/teks) | "Papan skor" (konkret) | Paham & pakai | Lancar |
| Ubah angka & lihat efek | **Sangat suka** | Suka | Suka |
| Sub-event (bersarang) | Lihat gambarnya saja | Membaca dengan bimbingan | Membaca & membuat |
| `Status` (mode/state machine) | Analogi lampu lalu lintas | Paham idenya | **Bisa merancang** |
| Array/soal, acak, Repeat | — (cukup melihat) | Idenya saja | Bisa dibimbing |
| Peta acak / Tween / Storage | Nikmati hasilnya | Demo + kagum | Telusuri & ubah 1 angka |

**Ringkas peran alami:** 8 th = **seniman + penguji + pembaca aturan**; 10 th = **perakit objek
& penulis event sederhana**; 12 th = **perancang logika (event, sarang, Status)**. Peran ini
kita jadikan **identitas tetap** di [Bagian 3](#3-model-studio-mini--tiga-peran-berbeda-yang-saling-mengunci).

> **Karena dasar mereka sudah ada** (sudah main & paham bentuk JIKA–MAKA), Sesi 1 boleh
> dipadatkan — langsung bagikan peran (Bagian 3) dan mulai membangun dari Sesi 2.

---

## 2. Dua mode mengajar

**Mode A — Bareng, satu proyek (disarankan untuk kalian bertiga).** Satu laptop, satu game
tumbuh bersama, tiap anak punya peran. Hemat, kolaboratif, dan tiap fitur jadi bahan diskusi.

**Mode B — Sendiri-sendiri.** Tiap anak proyek sendiri, maju sesuai kecepatan. Cocok kalau ada
2+ laptop, atau untuk yang 12 th ingin lari lebih cepat sambil yang lain berkolaborasi.

Kamu boleh mulai Mode A, lalu melepas si 12 th ke Mode B saat ia sudah mandiri.

---

## 3. Model Studio Mini — tiga peran berbeda yang saling mengunci

Perlakukan kalian sebagai **studio game kecil**. Tiap anak punya **peran tetap** dan
**wilayah miliknya sendiri** — bukan sekadar giliran. Ini memberi rasa **bangga & tanggung
jawab**, dan yang terpenting: **satu fitur baru butuh ketiganya**, jadi mereka harus bekerja sama.

### 🎨 Direktur Seni, Suara & Kualitas — **usia 8**
- **Wilayahmu:** semua yang *dilihat & didengar*, dan **memastikan game tidak rusak**.
- **Hidup di:** editor gambar/rekam suara, folder `assets/` & `audio/`, dan tombol **Preview (▶)**.
- **Tugas inti:** menggambar tokoh/telur/pohon; merekam suara (narator, kelinci, bacaan);
  mengganti file aset; **menguji tiap perubahan** & melaporkan bug; **membaca event keras-keras**.
- **Selesai kalau:** ada karya/suaramu di game, dan kamu sudah menekan Preview memastikannya jalan.

### 🧩 Desainer & Perakit Dunia — **usia 10**
- **Wilayahmu:** *isi* panggung — objek, penataan, variabel, dan "rasa" permainan.
- **Hidup di:** daftar **Objects**, tab **Scene**, panel **Variables**, objek **Text**.
- **Tugas inti:** menambah objek & behavior; menaruh instance; membuat & menampilkan variabel;
  mengetik teks; menyetel angka (kecepatan, jumlah, target) agar terasa pas.
- **Selesai kalau:** objek yang dibutuhkan sudah ada di scene dengan rapi dan variabelnya siap dipakai.

### ⚙️ Insinyur Logika (Programmer) — **usia 12**
- **Wilayahmu:** *aturan* — semua Event, dan bagaimana game "berpikir".
- **Hidup di:** tab **Events**, kondisi & aksi, `Status`, sarang (sub-event).
- **Tugas inti:** menulis Event (JIKA/MAKA), memakai **DAN**/**TIDAK**, menyusun **sarang**,
  merancang **mode `Status`**; menyambungkan pekerjaan seniman & perakit menjadi mekanik yang jalan.
- **Selesai kalau:** aturannya jalan sesuai maksud, dan kamu bisa **menjelaskan alurnya** ke adik.

### Alur "handoff": satu fitur butuh ketiganya

Contoh menambah fitur *"kelinci tersenyum saat jawaban benar"*:

```
🎨 (8)  gambar wajah kelinci tersenyum + rekam suara "Hebat!"      -> file aset & audio
   |
🧩 (10) tambah/atur objek kelinci di scene, siapkan variabelnya    -> dunia siap
   |
⚙️ (12) tulis event: JIKA jawaban benar MAKA tampilkan senyum + suara
   |
🎨 (8)  tekan Preview, uji, lapor: "sudah muncul!" / "belum, ini bug-nya"
```

Tempel alur ini di dinding. Tiap fitur baru mengikuti rantai yang sama — **tak ada peran yang
bisa jalan sendiri**, itulah inti kerja tim.

### Supaya spesialisasi tak mengurung (ritual bersama)

Peran tetap, tapi **semua tetap belajar logika** lewat 3 ritual kecil:
1. **Baca event keras-keras** di awal tiap sesi — dilakukan **semua**, dipimpin bergantian.
2. **Tukar kursi 5 menit** sekali per sesi: si 8/10 mencoba menulis satu kondisi sederhana dengan
   dibimbing si 12; si 12 sesekali menggambar/merekam. Cukup untuk *mencicipi* wilayah lain.
3. **Rapat 2 menit** di awal: "hari ini kita bikin fitur apa, dan siapa mengerjakan bagian mana?"

### Peran itu tumbuh (naik pangkat)

Seiring waktu, geser tanggung jawab ke atas: **8** mulai berani merakit objek kecil; **10** mulai
menulis event sendiri (pakai TIDAK/Invert); **12** mulai merancang sistem (array soal, peta).
Rayakan "kenaikan pangkat" ini.

### Papan kredit (rasa memiliki)

Buat scene/teks **"Dibuat oleh"** di game, atau file `CREDITS.txt`, cantumkan **nama + peran**
tiap anak (Direktur Seni, Perakit Dunia, Insinyur Logika). Ini menutup tiap proyek dengan bangga.

> **Aturan mouse:** mouse dipegang **pemilik tugas** saat itu; yang lain **mendikte langkah**
> ("sekarang klik Add condition…"), bukan merebut. Semua ikut berpikir, tak ada yang cuma menonton.

---

## 4. Alur sesi step-by-step (kurikulum 8 sesi)

Tiap sesi: **Tujuan → Kegiatan bersama → Adaptasi usia → Tanda paham.** Angka pelajaran
merujuk `MULAI-DARI-SINI.md`.

### Sesi 1 — Main dulu & bahasa "JIKA–MAKA" (Level 0.1)
- **Tujuan:** paham *apa* yang terjadi, dan kenal bentuk aturan JIKA–MAKA.
- **Bersama:** mainkan Telur Wazan (`build-web`) 10–15 menit. Lalu buka satu Event di GDevelop
  dan lihat gambar **anatomi event** (`docs/img/anatomi-event.svg`).
- **Adaptasi:** **8** menyebut objek yang ia lihat & membaca satu aturan keras-keras; **10**
  menemukan bagian JIKA vs MAKA; **12** membuka tab Events, menunjuk satu event dan menceritakan alurnya.
- **Tanda paham:** semua bisa berkata *"JIKA … MAKA …"* untuk satu kejadian di game.

### Sesi 2 — Bikin game sendiri: jalan & kumpulkan (Level 1: pel. 1–5)
- **Tujuan:** Objek + Behavior + Event collision pertama.
- **Bersama:** buat proyek baru "Tangkap Bintang": `Tokoh` (Top-down), beberapa `Bintang`,
  `TeksSkor`, variabel `Skor`, event *JIKA sentuh Bintang MAKA hapus + skor +1*.
- **Adaptasi:** **8** menggambar Tokoh & Bintang, lalu menekan Preview & menguji; **10** merakit
  objek + variabel + teks; **12** menulis event collision-nya (sambil menjelaskan tiap kondisi).
- **Tanda paham:** jalan ke bintang → hilang, skor naik.

### Sesi 3 — Menang, hidup, & suara mereka (pel. 6, 7, 9)
- **Tujuan:** kondisi angka (menang), animasi, suara rekaman sendiri.
- **Bersama:** event *JIKA Skor ≥ 3 MAKA tampilkan MENANG*; animasi `diam`/`jalan`; suara "dapat".
- **Adaptasi:** **8** merekam suara ("Hore!", "Dapat!") & menggambar frame jalan; **10** membuat
  2 event animasi (pakai **TIDAK**/Invert); **12** event menang + merapikan.
- **Tanda paham:** ada suara anak sendiri, tokoh bergerak beda saat jalan/diam, muncul MENANG.

### Sesi 4 — Kamera, layer UI, tombol & pindah scene (pel. 8, 10, 11, 12)
- **Tujuan:** dunia lebih besar dari layar; menu & berpindah scene.
- **Bersama:** kepala mengikuti badan; kamera mengikuti; skor di layer `UI`; scene `Menu` +
  tombol → *Change scene*.
- **Adaptasi:** **8** menguji "apakah skor ikut geser?"; **10** membuat layer UI & tombol;
  **12** event klik-tombol (cursor on object **DAN** klik) + pindah scene.
- **Tanda paham:** mulai dari Menu → klik → masuk game; skor diam di pojok.

### Sesi 5 — Tiap tombol bawa angkanya & waktu (pel. 13, 14)
- **Tujuan:** variabel objek (instance) + timer.
- **Bersama:** 3 tombol dengan variabel objek `nomor` (1/2/3) → set `Pilihan`; pesan yang muncul
  2 detik lalu hilang (timer).
- **Adaptasi:** **8** menekan tiap tombol & memastikan papan mengingat angka yang benar; **10**
  memberi variabel `nomor` ke tiap instance; **12** event + timer.
- **Tanda paham:** klik tombol 3 → papan menampilkan 3; pesan hilang sendiri.

### Sesi 6 — "Mode" permainan: `Status` (pel. 15) — inti
- **Tujuan:** state machine — satu variabel menyetir semua, dijaga tiap event.
- **Bersama:** tambah variabel `Status`; beri event gameplay kondisi `Status = "main"`; buat satu
  keadaan `"jeda"`. Pakai analogi **lampu lalu lintas**.
- **Adaptasi:** **12** merancang & menulis (fokus utama); **10** mengamati dan menambahkan satu
  kondisi penjaga; **8** menjadi "lampu" dalam main peran (hijau=boleh gerak, merah=berhenti).
- **Tanda paham:** saat `Status` bukan `"main"`, tokoh berhenti sendiri. **Ini konsep terpenting
  untuk memahami scene Hutan.**

### Sesi 7 — Daftar soal, acak, & sarang (pel. 16, 17) + gambar bersarang
- **Tujuan:** array + structure + Random + Repeat + membaca **sub-event**.
- **Bersama:** buat array `Daftar` berisi structure (`teks`, `benar`); ambil acak; ubah "Tangkap
  Bintang" jadi **mini-kuis** (sentuh bintang → muncul pertanyaan). Lihat gambar
  **bersarang** (`docs/img/bersarang.svg`).
- **Adaptasi:** **12** membuat array & event bersarang; **10** melihat & menjelaskan ulang
  sarangnya; **8** mengisi isi soal (menyumbang pertanyaan) & menguji.
- **Tanda paham:** 12 th bisa menjelaskan "kenapa Repeat ada di dalam event, dan pengecek ada di
  dalam Repeat".

### Sesi 8 — Buka Telur Wazan yang asli (`TUTORIAL.md`)
- **Tujuan:** sadar bahwa game asli = semua yang mereka bangun, digabung & diperbesar.
- **Bersama:** buka `game.json`. Telusuri: ubah `TargetTelur` jadi 3; ganti satu gambar & satu
  suara dengan **karya mereka**; buka Events scene Hutan dan **baca** satu event bersarang.
- **Adaptasi:** **8** mengganti aset/suara & bermain; **10** menemukan variabel & mengubah teks;
  **12** menelusuri grup "Buat peta acak" dan mengubah satu angka (Tween/Storage cukup **didemokan**).
- **Tanda paham:** mereka menunjuk fitur di Telur Wazan dan berkata *"ini seperti yang kita buat
  di Sesi …"*.

> Setelah Sesi 8, ulang **latihan bertahap** di `TUTORIAL.md` Bagian 12 sebagai proyek lanjutan
> (tambah soal, event baru, peta, tingkat boneka, scene baru).

---

## 5. Kalimat siap pakai (skrip untuk momen kunci)

- **Mengenalkan event:** "Komputer punya buku aturan. Tiap aturan bentuknya sama: **JIKA** ini
  terjadi, **MAKA** lakukan itu. Ayo baca satu bareng."
- **Saat error:** "Bagus, kita nemu sesuatu! Coba baca aturannya keras-keras. Menurutmu aturan
  ini menyuruh komputer melakukan apa?"
- **Mengenalkan `Status`:** "Bayangkan lampu lalu lintas. Kalau **hijau** (mode `main`) boleh
  jalan. Kalau **merah** (mode `soal`) berhenti, jawab dulu. `Status` itu warnanya."
- **Mengenalkan sarang:** "Aturan yang **menjorok ke dalam** hanya dicek kalau aturan di atasnya
  benar dulu — seperti 'kalau pintu terbuka, baru periksa: ada tamu atau tidak?'."
- **Menjaga giliran:** "Sekarang giliran … pegang mouse. Yang lain jadi 'peta': kasih tahu
  langkahnya, jangan ambil mouse-nya."

---

## 6. Ceklis "sudah paham kalau…" (per usia)

**8 tahun**
- [ ] Bisa mengubah satu angka lalu menebak & memeriksa efeknya lewat Preview.
- [ ] Bisa membaca satu event dalam bentuk "JIKA … MAKA …".
- [ ] Berhasil memasukkan gambar/suara buatannya ke game.

**10 tahun**
- [ ] Bisa menambah objek + variabel dan menampilkannya di teks.
- [ ] Bisa menulis satu event sendiri (termasuk memakai **TIDAK**/Invert).
- [ ] Bisa menjelaskan beda Objek vs Instance, dan apa itu variabel.

**12 tahun**
- [ ] Bisa merancang beberapa event dengan `Status` sebagai penjaga.
- [ ] Bisa **membaca & membuat** event bersarang, dan menjelaskan alurnya.
- [ ] Bisa menelusuri Telur Wazan dan menemukan event yang bertanggung jawab atas suatu kejadian.

---

## 7. Manajemen sesi (praktis)

- **Simpan sering** (Ctrl+S). Tiap akhir sesi, **salin folder** proyek sebagai cadangan
  (mis. `game-sesi3/`) supaya eksperimen berani tanpa takut merusak.
- **Aturan Undo:** "tanya dulu sebelum Ctrl+Z berkali-kali" — supaya kerja bareng tak hilang.
- **Timer giliran mouse:** 5–10 menit per anak, lalu putar.
- **Papan "aturan hari ini":** tulis 1 event yang dipelajari di kertas, tempel. Akhir pekan,
  lihat berapa aturan yang sudah dikuasai.
- **Berhenti mumpung seru.** Tinggalkan satu ide untuk sesi berikutnya ("besok kita bikin
  suaranya ya").

---

## 8. Sekalian belajar shorof (jangan lupa tujuannya)

Game ini alat, bukan tujuan. Saat bermain/menyusun soal, kaitkan ke materinya sesuai usia:
- **8 th:** kenali **bunyi & bentuk** wazan (dengarkan, tirukan, cocokkan gambar/warna wazan).
- **10 th:** **cocokkan pola** — "fi'il ini ikut wazan yang mana?" tanpa harus menjelaskan alasan.
- **12 th:** **jelaskan alasannya** — kenapa fi'il masuk bab tertentu (pola harakat `fa-'a-la`),
  lalu ia bisa menambah soal baru yang benar ke daftar `Soal`.

> Momen terbaik: saat menjawab telur, **jeda** dan tanya *"kenapa ini masuk / tidak masuk
> wazan yang dicari?"* — di situ game berubah jadi pelajaran shorof.
