# Panduan Mengajar — Alur Tutoring Berbasis Peran (Studio Game Mini)

Cara **step-by-step** mengajarkan GDevelop lewat game ini untuk beberapa anak sekaligus.
Prinsip utamanya: **peran ditentukan oleh bakat & minat, BUKAN usia.** Anak mana pun bisa
menjadi Insinyur Logika — sering kali justru yang tak terduga.

Dipakai bersama:
- **`MULAI-DARI-SINI.md`** — kursus Level 0–4 (bikin "Telur Wazan mini" dari nol).
- **`TUTORIAL.md`** — membedah Telur Wazan yang asli.

---

## 0. Lima prinsip mengajar

1. **Satu perubahan → tekan Preview → "apa yang berubah?"** Ini ritme belajarnya.
2. **Baca event keras-keras** sebelum mengeklik: *"JIKA apa? MAKA apa? ada sarang tidak?"*
3. **Rayakan error.** Layar rusak = momen belajar terbaik: "aturan tadi bilang apa?"
4. **Anak harus merasa memiliki.** Beri mereka menggambar aset & merekam suara sesegera mungkin.
5. **Sesi pendek, berhenti saat masih seru.** Sesuaikan durasi dengan fokus tiap anak, bukan umurnya.

---

## 1. Tiga bakat & cara mengenalinya (tanpa melihat umur)

Amati **kecenderungan alami** tiap anak. Ini petunjuk, bukan label — bakat bisa tumpang tindih
dan berubah seiring waktu.

| Bakat | Tanda-tandanya (perhatikan yang mana "berbinar matanya") |
|---|---|
| 🎨 **Seni, Suara & Ketelitian** | Suka menggambar/mewarnai, peka detail visual, senang bunyi/suara, telaten mencoba berulang & menemukan yang "aneh" (bug). |
| 🧩 **Menata & Merakit** | Suka merapikan, menata tata letak, menyetel angka ("kalau lebih cepat lebih seru"), senang melihat semuanya "pas". |
| ⚙️ **Logika & Sebab-akibat** | Suka teka-teki, sering bertanya *"kenapa?"* / *"gimana kalau…?"*, senang aturan & pola, tahan berpikir saat menemui masalah. |

> **Penting:** ketiganya **tidak terikat umur**. Si bungsu bisa jadi Insinyur; si sulung bisa jadi
> Direktur Seni. Ikuti bakatnya, bukan tanggal lahirnya.

---

## 2. Cara menemukan peran tiap anak

Peran boleh **cair** (bisa berganti), tapi paling baik ditemukan lewat mencoba:

1. **Coba dulu (try-out).** Di 1–2 sesi awal, biarkan **tiap anak mencicipi tiap wilayah**
   (gambar, rakit objek, tulis satu event). Perhatikan yang mana paling membuat mereka asyik.
2. **Ikuti minat.** Peran terbaik = yang bikin anak **lupa waktu** dan ingin melanjutkan sendiri.
3. **Biarkan memilih.** Setelah mencicipi, minta mereka memilih peran. Rasa memilih = rasa memiliki.
4. **Boleh tukar.** Kalau seorang anak penasaran wilayah lain, izinkan pindah. Bakat bisa muncul
   belakangan — terutama Logika, yang kadang baru "klik" setelah beberapa sesi.

> Kalau ada dua anak menginginkan peran yang sama, jadikan mereka **duet** di peran itu
> (mis. dua Insinyur bergiliran menulis event) daripada memaksa salah satu pindah.

---

## 3. Model Studio Mini — tiga peran yang saling mengunci

Perlakukan kalian sebagai **studio game kecil**. Tiap anak memegang **satu peran** dengan
**wilayah miliknya sendiri**. Yang terpenting: **satu fitur baru butuh ketiga peran**, jadi
mereka harus bekerja sama.

### 🎨 Direktur Seni, Suara & Kualitas
- **Cocok untuk anak yang:** suka menggambar, suara, dan teliti mencari yang tidak beres.
- **Wilayahmu:** semua yang *dilihat & didengar*, dan **memastikan game tidak rusak**.
- **Hidup di:** editor gambar/rekam suara, folder `assets/` & `audio/`, tombol **Preview (▶)**.
- **Tugas inti:** menggambar tokoh/telur/pohon; merekam suara (narator, kelinci, bacaan);
  mengganti file aset; **menguji tiap perubahan** & melaporkan bug; **membaca event keras-keras**.
- **Selesai kalau:** ada karya/suaramu di game, dan kamu sudah menekan Preview memastikannya jalan.

### 🧩 Desainer & Perakit Dunia
- **Cocok untuk anak yang:** suka menata, merapikan, dan menyetel sampai "terasa pas".
- **Wilayahmu:** *isi* panggung — objek, penataan, variabel, dan "rasa" permainan.
- **Hidup di:** daftar **Objects**, tab **Scene**, panel **Variables**, objek **Text**.
- **Tugas inti:** menambah objek & behavior; menaruh instance; membuat & menampilkan variabel;
  mengetik teks; menyetel angka (kecepatan, jumlah, target) agar terasa pas.
- **Selesai kalau:** objek yang dibutuhkan sudah ada di scene dengan rapi dan variabelnya siap dipakai.

### ⚙️ Insinyur Logika (Programmer)
- **Cocok untuk anak yang:** suka teka-teki, bertanya "kenapa/gimana kalau", tahan berpikir.
- **Wilayahmu:** *aturan* — semua Event, dan bagaimana game "berpikir".
- **Hidup di:** tab **Events**, kondisi & aksi, `Status`, sarang (sub-event).
- **Tugas inti:** menulis Event (JIKA/MAKA), memakai **DAN**/**TIDAK**, menyusun **sarang**,
  merancang **mode `Status`**; menyambungkan pekerjaan seniman & perakit menjadi mekanik yang jalan.
- **Selesai kalau:** aturannya jalan sesuai maksud, dan kamu bisa **menjelaskan alurnya** ke yang lain.

### Alur "handoff": satu fitur butuh ketiganya

Contoh menambah fitur *"kelinci tersenyum saat jawaban benar"*:

```
🎨  gambar wajah kelinci tersenyum + rekam suara "Hebat!"       -> file aset & audio
   |
🧩  tambah/atur objek kelinci di scene, siapkan variabelnya     -> dunia siap
   |
⚙️  tulis event: JIKA jawaban benar MAKA tampilkan senyum + suara
   |
🎨  tekan Preview, uji, lapor: "sudah muncul!" / "belum, ini bug-nya"
```

Tempel alur ini di dinding. Tiap fitur baru mengikuti rantai yang sama — **tak ada peran yang
bisa jalan sendiri**, itulah inti kerja tim.

### Supaya spesialisasi tak mengurung (ritual bersama)

Peran tetap, tapi **semua tetap belajar logika** lewat 3 ritual kecil:
1. **Baca event keras-keras** di awal tiap sesi — dilakukan **semua**, dipimpin bergantian.
2. **Tukar kursi 5 menit** sekali per sesi: yang non-Insinyur mencoba menulis satu kondisi
   sederhana (dibimbing Insinyur); Insinyur sesekali menggambar/merekam. Cukup untuk *mencicipi*.
3. **Rapat 2 menit** di awal: "hari ini kita bikin fitur apa, dan siapa mengerjakan bagian mana?"

### Peran itu tumbuh (naik pangkat)

Dorong tiap anak melampaui wilayahnya sedikit demi sedikit: Seniman mulai berani merakit objek;
Perakit mulai menulis event sendiri (pakai TIDAK/Invert); Insinyur mulai merancang sistem (array
soal, peta). Rayakan tiap "kenaikan pangkat".

### Papan kredit (rasa memiliki)

Buat scene/teks **"Dibuat oleh"** di game, atau file `CREDITS.txt`, cantumkan **nama + peran**
tiap anak. Ini menutup tiap proyek dengan bangga.

> **Aturan mouse:** mouse dipegang **pemilik tugas** saat itu; yang lain **mendikte langkah**
> ("sekarang klik Add condition…"), bukan merebut. Semua ikut berpikir, tak ada yang cuma menonton.

---

## 4. Dua mode mengajar

**Mode A — Bareng, satu proyek (disarankan).** Satu laptop, satu game tumbuh bersama, tiap anak
punya peran. Hemat, kolaboratif, tiap fitur jadi bahan diskusi.

**Mode B — Sendiri-sendiri.** Tiap anak proyek sendiri, maju sesuai kecepatannya. Cocok kalau ada
2+ laptop, atau untuk anak yang ingin lari lebih cepat sambil yang lain berkolaborasi.

Boleh mulai Mode A, lalu melepas anak yang sudah mandiri ke Mode B.

---

## 5. Alur sesi step-by-step (kurikulum 8 sesi)

Tiap sesi: **Tujuan → Kegiatan bersama → Bagian tiap peran → Tanda paham.** Angka pelajaran
merujuk `MULAI-DARI-SINI.md`. (Kalau dasar mereka sudah kuat, padatkan Sesi 1 dan langsung membangun.)

### Sesi 1 — Main dulu & bahasa "JIKA–MAKA" (Level 0.1)
- **Tujuan:** paham *apa* yang terjadi, kenal bentuk aturan JIKA–MAKA, **cicipi tiap wilayah**
  untuk menemukan peran (Bagian 2).
- **Bersama:** mainkan Telur Wazan (`build-web`) 10–15 menit. Buka satu Event & lihat
  **anatomi event** (`docs/img/anatomi-event.svg`). Lalu tiap anak mencoba sedikit: menggambar,
  menaruh objek, membaca satu event.
- **Tanda paham:** semua bisa berkata *"JIKA … MAKA …"* untuk satu kejadian; mulai terlihat siapa
  condong ke peran mana.

### Sesi 2 — Bikin game sendiri: jalan & kumpulkan (Level 1: pel. 1–5)
- **Tujuan:** Objek + Behavior + Event collision pertama.
- **Bersama:** buat proyek "Tangkap Bintang": `Tokoh` (Top-down), beberapa `Bintang`, `TeksSkor`,
  variabel `Skor`, event *JIKA sentuh Bintang MAKA hapus + skor +1*.
- **Bagian tiap peran:** 🎨 menggambar Tokoh & Bintang, lalu uji; 🧩 merakit objek + variabel + teks;
  ⚙️ menulis event collision (sambil menjelaskan tiap kondisi).
- **Tanda paham:** jalan ke bintang → hilang, skor naik.

### Sesi 3 — Menang, hidup, & suara mereka (pel. 6, 7, 9)
- **Tujuan:** kondisi angka (menang), animasi, suara rekaman sendiri.
- **Bersama:** event *JIKA Skor ≥ 3 MAKA tampilkan MENANG*; animasi `diam`/`jalan`; suara "dapat".
- **Bagian tiap peran:** 🎨 rekam suara & gambar frame jalan; 🧩 rakit objek teks "MENANG";
  ⚙️ event menang + 2 event animasi (pakai **TIDAK**/Invert).
- **Tanda paham:** ada suara anak, tokoh bergerak beda saat jalan/diam, muncul MENANG.

### Sesi 4 — Kamera, layer UI, tombol & pindah scene (pel. 8, 10, 11, 12)
- **Tujuan:** dunia lebih besar dari layar; menu & berpindah scene.
- **Bersama:** kepala mengikuti badan; kamera mengikuti; skor di layer `UI`; scene `Menu` +
  tombol → *Change scene*.
- **Bagian tiap peran:** 🎨 uji "apakah skor ikut geser?"; 🧩 buat layer UI & tombol;
  ⚙️ event klik-tombol (cursor on object **DAN** klik) + pindah scene.
- **Tanda paham:** mulai dari Menu → klik → masuk game; skor diam di pojok.

### Sesi 5 — Tiap tombol bawa angkanya & waktu (pel. 13, 14)
- **Tujuan:** variabel objek (instance) + timer.
- **Bersama:** 3 tombol dengan variabel objek `nomor` (1/2/3) → set `Pilihan`; pesan yang muncul
  2 detik lalu hilang (timer).
- **Bagian tiap peran:** 🎨 uji tiap tombol mengingat angka yang benar; 🧩 beri variabel `nomor`
  ke tiap instance; ⚙️ event + timer.
- **Tanda paham:** klik tombol 3 → papan menampilkan 3; pesan hilang sendiri.

### Sesi 6 — "Mode" permainan: `Status` (pel. 15) — inti
- **Tujuan:** state machine — satu variabel menyetir semua, dijaga tiap event.
- **Bersama:** tambah variabel `Status`; beri event gameplay kondisi `Status = "main"`; buat satu
  keadaan `"jeda"`. Analogi **lampu lalu lintas**.
- **Bagian tiap peran:** ⚙️ merancang & menulis (fokus utama); 🧩 menambah satu kondisi penjaga;
  🎨 jadi "lampu" dalam main peran (hijau=boleh gerak, merah=berhenti) & menguji.
- **Tanda paham:** saat `Status` bukan `"main"`, tokoh berhenti sendiri. **Konsep terpenting untuk
  memahami scene Hutan.**

### Sesi 7 — Daftar soal, acak, & sarang (pel. 16, 17)
- **Tujuan:** array + structure + Random + Repeat + membaca **sub-event**.
- **Bersama:** array `Daftar` berisi structure (`teks`, `benar`); ambil acak; ubah jadi
  **mini-kuis** (sentuh bintang → muncul pertanyaan). Lihat gambar **bersarang**
  (`docs/img/bersarang.svg`).
- **Bagian tiap peran:** ⚙️ membuat array & event bersarang; 🧩 menjelaskan ulang sarangnya;
  🎨 mengisi isi soal (menyumbang pertanyaan) & menguji.
- **Tanda paham:** Insinyur bisa menjelaskan "kenapa Repeat ada di dalam event, dan pengecek di dalam Repeat".

### Sesi 8 — Buka Telur Wazan yang asli (`TUTORIAL.md`)
- **Tujuan:** sadar bahwa game asli = semua yang mereka bangun, digabung & diperbesar.
- **Bersama:** buka `game.json`. Ubah `TargetTelur` jadi 3; ganti satu gambar & satu suara dengan
  **karya mereka**; buka Events scene Hutan dan **baca** satu event bersarang.
- **Bagian tiap peran:** 🎨 mengganti aset/suara & bermain; 🧩 menemukan variabel & mengubah teks;
  ⚙️ menelusuri grup "Buat peta acak" dan mengubah satu angka (Tween/Storage cukup **didemokan**).
- **Tanda paham:** mereka menunjuk fitur di Telur Wazan dan berkata *"ini seperti yang kita buat di Sesi …"*.

> Setelah Sesi 8, ulang **latihan bertahap** di `TUTORIAL.md` Bagian 12 sebagai proyek lanjutan.

---

## 6. Kalimat siap pakai (skrip untuk momen kunci)

- **Mengenalkan event:** "Komputer punya buku aturan. Tiap aturan bentuknya sama: **JIKA** ini
  terjadi, **MAKA** lakukan itu. Ayo baca satu bareng."
- **Saat error:** "Bagus, kita nemu sesuatu! Coba baca aturannya keras-keras. Menurutmu aturan
  ini menyuruh komputer melakukan apa?"
- **Mengenalkan `Status`:** "Bayangkan lampu lalu lintas. **Hijau** (mode `main`) boleh jalan.
  **Merah** (mode `soal`) berhenti, jawab dulu. `Status` itu warnanya."
- **Mengenalkan sarang:** "Aturan yang **menjorok ke dalam** hanya dicek kalau aturan di atasnya
  benar dulu — seperti 'kalau pintu terbuka, baru periksa: ada tamu atau tidak?'."
- **Menemukan bakat:** "Coba semua dulu. Bagian mana yang bikin kamu paling betah? Itu mungkin peranmu."

---

## 7. Ceklis "sudah paham kalau…" (per peran, bukan per umur)

**🎨 Direktur Seni, Suara & Kualitas**
- [ ] Bisa memasukkan gambar/suara buatannya sendiri ke game.
- [ ] Bisa menekan Preview, menemukan yang tidak beres, dan menjelaskannya ("ini bug-nya").
- [ ] Bisa membaca satu event dalam bentuk "JIKA … MAKA …".

**🧩 Desainer & Perakit Dunia**
- [ ] Bisa menambah objek + variabel dan menampilkannya di teks.
- [ ] Bisa menata scene & menyetel angka sampai "terasa pas".
- [ ] Bisa menjelaskan beda Objek vs Instance, dan apa itu variabel.

**⚙️ Insinyur Logika**
- [ ] Bisa menulis event sendiri (termasuk **DAN** dan **TIDAK**/Invert).
- [ ] Bisa **membaca & membuat** event bersarang, dan menjelaskan alurnya.
- [ ] Bisa merancang beberapa event dengan `Status` sebagai penjaga, dan menemukan event yang
      bertanggung jawab atas suatu kejadian di Telur Wazan.

---

## 8. Manajemen sesi (praktis)

- **Simpan sering** (Ctrl+S). Tiap akhir sesi, **salin folder** proyek sebagai cadangan
  (mis. `game-sesi3/`) supaya berani bereksperimen tanpa takut merusak.
- **Aturan Undo:** "tanya dulu sebelum Ctrl+Z berkali-kali" — supaya kerja bareng tak hilang.
- **Papan "aturan hari ini":** tulis 1 event yang dipelajari di kertas, tempel. Lihat berapa yang
  sudah dikuasai tiap pekan.
- **Berhenti mumpung seru.** Tinggalkan satu ide untuk sesi berikutnya.

---

## 9. Sekalian belajar shorof (jangan lupa tujuannya)

Game ini alat, bukan tujuan. Kaitkan ke materi sesuai **kesiapan tiap anak** (bukan umurnya):

- **Tahap kenal:** dengarkan & tirukan **bunyi** wazan; cocokkan **gambar/warna** wazan.
- **Tahap pola:** "fi'il ini ikut wazan yang mana?" — mencocokkan pola tanpa perlu menjelaskan alasan.
- **Tahap paham:** **jelaskan alasannya** — kenapa fi'il masuk bab tertentu (pola harakat), lalu
  bisa menambah soal baru yang benar ke daftar `Soal`.

> Momen terbaik: saat menjawab telur, **jeda** dan tanya *"kenapa ini masuk / tidak masuk wazan
> yang dicari?"* — di situ game berubah jadi pelajaran shorof.
