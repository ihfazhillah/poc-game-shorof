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

## 5. Kurikulum 8 sesi — membangun "Telur Wazan Mini"

Alih-alih game latihan yang lepas, 8 sesi ini membangun **versi sederhana dari Telur Wazan yang
asli** — memakai **aset & data fi'il yang sama**, tapi mekaniknya dipangkas. Jadi saat membuka
game penuh nanti, hampir semuanya sudah dikenal. Teknik dasar tiap langkah dijelaskan terpisah di
`MULAI-DARI-SINI.md` (ditunjuk sebagai "teknik: pel. X" bila ingin latihan konsepnya lebih dulu).

> **Anak-anak yang sudah pernah main Telur Wazan (seperti kasusmu):** Sesi 1 tinggal ~10 menit
> **pembuka** (temukan peran + lihat anatomi event + sepakati target) — **tidak perlu diajari main
> lagi**. Pembangunan sesungguhnya **mulai Sesi 2**. Jadi efektif ada **7 sesi membangun (2–8)**.

> **Aset gratis:** mulai proyek **baru**, lalu impor gambar dari folder **`assets/`** repo ini
> (petualang, telur, rumput, pohon, panel_soal, tombol_ya/tidak, keranjang). 🎨 boleh menimpanya
> dengan gambar sendiri kapan saja.

### 5a. Yang kita bangun vs yang kita tinggalkan (untuk sekarang)

| Bagian | Telur Wazan **Mini** (yang kita buat) | Telur Wazan **penuh** |
|---|---|---|
| Petualang berjalan | ✅ top-down, aset asli | ✅ + kepala terpisah |
| Hutan | ✅ latar rumput + beberapa pohon **ditaruh tangan** | ✅ **peta acak** (procedural) |
| Telur → soal | ✅ | ✅ + peta mini |
| Pilih fi'il | ✅ acak dari ~6 soal | ✅ acak **seimbang** dari 81 |
| Jawab YA/TIDAK → benar/salah | ✅ (pesan sederhana) | ✅ + adegan bertahap (asap, kelinci) |
| Menang | ✅ saat skor cukup | ✅ harus **sampai FINISH** |
| Suara | 🎨 rekam sendiri | rekaman / edge-tts |
| Boneka koleksi + simpan | ❌ nanti | ✅ Storage |
| Telur terbang ke keranjang | ❌ nanti | ✅ Tween |

### 5b. Data awal (salin dari daftar Telur Wazan — 2 wazan, 6 fi'il)

Variabel global **`NamaBab`** (array teks): `["فَعَلَ - يَفْعُلُ", "فَعِلَ - يَفْعَلُ"]`

Variabel global **`Soal`** (array structure `madhi`, `mudhari`, `arti`, `bab`):

| madhi | mudhari | arti | bab |
|---|---|---|---|
| نَصَرَ | يَنْصُرُ | menolong | 1 |
| كَتَبَ | يَكْتُبُ | menulis | 1 |
| دَخَلَ | يَدْخُلُ | masuk | 1 |
| عَلِمَ | يَعْلَمُ | mengetahui | 2 |
| شَرِبَ | يَشْرَبُ | minum | 2 |
| سَمِعَ | يَسْمَعُ | mendengar | 2 |

Plus variabel global **`BabTarget`** (1 atau 2) dan **`TargetTelur`** (mis. 3).

*(Dua wazan yang jelas beda ini membuat jawaban YA/TIDAK bermakna. Nanti tinggal tambah baris untuk
memperbanyak soal — persis seperti game penuh.)*

### Sesi 1 — Pembuka singkat (lewati main-nya kalau sudah pernah)
- **Tujuan:** **cicipi tiap wilayah** untuk menemukan peran (Bagian 2), dan sepakati "kita akan
  membuat versi mini game ini".
- **Kalau sudah pernah main** (kasusmu): langsung ~10 menit — buka satu Event & lihat **anatomi
  event** (`docs/img/anatomi-event.svg`), lalu tunjuk fitur mana yang akan dibuat vs ditinggalkan
  (tabel 5a). *Belum pernah main?* Mainkan dulu `build-web` 10–15 menit.
- **Tanda paham:** semua bisa berkata *"JIKA … MAKA …"* untuk satu kejadian; mulai terlihat bakat.

> Sesudah ini, **mulai membangun dari Sesi 2.**

### Sesi 2 — Petualang berjalan di hutan (teknik: pel. 2, 10)
- **Tujuan:** Objek + Behavior + latar + kamera.
- **Bangun:** objek **`Petualang`** (aset `petualang_badan_*`, behavior **Top-down movement**);
  latar **`Rumput`** (Tiled) besar; beberapa **`Pohon`**; kamera **Center on `Petualang`**.
- **Peran:** 🎨 impor/gambar aset & uji; 🧩 taruh objek + atur kamera; ⚙️ pasang & setel behavior.
- **Tanda paham:** bisa berjalan di hutan, kamera mengikuti.

### Sesi 3 — Telur & skor (teknik: pel. 3, 4, 5, 7)
- **Tujuan:** collision + variabel + animasi.
- **Bangun:** taruh **3 `Telur`** (animasi `utuh`; `pecah` dari `telur_pecah1..3`). HUD
  **`TeksSkor`** "0 / 3" (variabel **`Skor`**). Event: *JIKA `Petualang` sentuh `Telur` MAKA
  Telur → "pecah", `Skor` +1, perbarui teks, hapus telur.* (Sementara belum ada soal.)
- **Peran:** 🎨 aset telur & uji; 🧩 HUD skor + variabel; ⚙️ event collision.
- **Tanda paham:** sentuh telur → pecah, skor naik.

### Sesi 4 — Telur memunculkan SOAL + mode `Status` (teknik: pel. 15, 11, 6) — inti
- **Tujuan:** state machine + panel + tombol.
- **Bangun:** variabel **`Status`** ("jalan"/"soal"). Objek di layer **`UI`**: `PanelSoal`,
  `TeksSoalArab`, `TeksPertanyaan`, `TombolYa`, `TombolTidak` (kelompokkan jadi grup `GrupSoal`,
  sembunyikan di awal). Ubah event telur: *JIKA `Status`="jalan" DAN sentuh Telur MAKA
  `Status`="soal", telur pecah, tampilkan `GrupSoal`* dengan **fi'il tetap** dulu (mis.
  نَصَرَ - يَنْصُرُ) + "Apakah termasuk wazan فَعَلَ - يَفْعُلُ؟". **Beri semua event gerak
  penjaga `Status`="jalan".**
- **Peran:** ⚙️ `Status` + penjaga (fokus); 🧩 rakit panel & tombol di layer UI; 🎨 uji "gerak
  berhenti saat panel muncul?".
- **Tanda paham:** sentuh telur → berjalan terkunci, panel soal muncul.

### Sesi 5 — Benar vs Salah (teknik: pel. 5 + sarang 0.5–0.6)
- **Tujuan:** cabang keputusan dengan `Kunci`/`Jawaban`.
- **Bangun:** variabel **`Kunci`**, **`Jawaban`**. Klik `TombolYa` → `Jawaban`="ya"; `TombolTidak`
  → "tidak". (Fi'il masih tetap; set `Kunci`="ya" manual.) Lalu: *JIKA `Jawaban` = `Kunci` MAKA
  benar (`Skor`+1, `Status`="jalan", hapus telur, suara "Benar")* ; *JIKA `Jawaban` ≠ `Kunci` MAKA
  salah (tampilkan wazan yang benar, suara "Salah", lalu `Status`="jalan")*.
- **Peran:** ⚙️ dua cabang (bersarang di bawah "sudah menjawab"); 🎨 rekam suara benar/salah & uji;
  🧩 rapikan teks pesan.
- **Tanda paham:** jawab benar → skor naik; salah → muncul wazan yang benar.

### Sesi 6 — Fi'il ACAK dari daftar (teknik: pel. 16) — inti data
- **Tujuan:** array + structure + Random (model data asli, versi kecil).
- **Bangun:** isi variabel global **`Soal`** (6 structure) & **`NamaBab`** (Bagian 5b); `BabTarget`=1.
  Saat telur pecah: `SoalIdx = Random(VariableChildCount(Soal) - 1)`; isi panel dari
  `Soal[SoalIdx].madhi`, `.mudhari`, `.arti`; **`Kunci` = "ya" jika `Soal[SoalIdx].bab` =
  `BabTarget`, selain itu "tidak"**.
- **Peran:** ⚙️ array + pemilihan acak + `Kunci` otomatis; 🧩 mengisi data `Soal`; 🎨 uji ragam fi'il.
- **Tanda paham:** fi'il berganti-ganti; jawaban YA/TIDAK jadi benar-benar bermakna.

### Sesi 7 — Menu pilih wazan + scene Menang (teknik: pel. 12, 13, 6)
- **Tujuan:** variabel objek + pindah scene + kondisi menang.
- **Bangun:** scene **`Menu`**: 2 `TombolBab` dengan **variabel objek `bab`** (1 & 2) + label wazan;
  klik → `BabTarget = TombolBab.bab` → scene `Hutan`. Scene **`Menang`**: dari Hutan, *JIKA `Skor`
  ≥ `TargetTelur` MAKA scene `Menang`* (teks "Hebat!" + tombol "Main lagi" → `Menu`).
- **Peran:** ⚙️ event tombol + menang; 🧩 tata scene Menu & Menang; 🎨 aset tombol/teks & uji alur.
- **Tanda paham:** pilih wazan → main → kumpulkan cukup → **Menang** → kembali ke Menu. **Ini sudah
  "Telur Wazan Mini" yang utuh.**

### Sesi 8 — Bandingkan dengan yang asli & poles (`TUTORIAL.md`)
- **Tujuan:** sadar game penuh = mini ini + beberapa tambahan.
- **Bersama:** buka `game.json` asli. Temukan tiap bagian mini di sana ("ini yang kita buat!"), lalu
  lihat yang **ditambahkan**: peta acak, kepala terpisah, telur terbang (Tween), boneka + simpan
  (Storage), adegan salah bertahap. Ganti aset/suara mini dengan karya mereka; baca satu event
  bersarang asli.
- **Peran:** 🎨 pasang aset/suara mereka & bermain; 🧩 temukan variabel & ubah teks; ⚙️ telusuri grup
  "Buat peta acak", ubah satu angka (Tween/Storage cukup **didemokan**).
- **Tanda paham:** menunjuk fitur asli dan berkata *"ini versi besar dari punya kita; yang baru cuma
  peta acak, boneka, dan animasi terbang."*

> Lanjutan: perbanyak soal (tambah baris di `Soal`), tambahkan satu per satu fitur penuh mengikuti
> `TUTORIAL.md` Bagian 8–11 (peta acak → tween → koleksi).

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
