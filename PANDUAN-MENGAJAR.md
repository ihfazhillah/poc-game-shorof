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

> **Karena anak belum kenal konsep programming**, kita mulai dari **yang terkecil yang sudah bisa
> dimainkan** — "Telur Wazan **Nano**" (Sesi 2, hanya **3 aturan**) — lalu **tumbuhkan satu konsep
> per sesi**, tiap kali karena ada kebutuhan yang mereka rasakan. (Nano bahkan lebih kecil dari
> kolom "Mini" di tabel 5a: belum ada skor, `Status`, daftar, menu, atau menang — semua itu
> ditambahkan bertahap di Sesi 3–7.)
>
> **Di awal, kamu (yang cepat paham) boleh memegang peran ⚙️ Insinyur** sambil anak mengerjakan
> 🎨 seni, 🧩 perakitan, dan pengujian; **serahkan logika bertahap** begitu ada anak yang mulai
> "klik". Aturan emas tetap: **satu langkah kecil → Preview → "apa yang berubah?"**

### Sesi 2 — "Telur Wazan Nano": versi terkecil yang sudah bisa dimainkan
- **Tujuan:** satu game utuh **paling kecil** — sentuh telur, muncul fi'il, jawab YA/TIDAK, benar/salah.
- **Bangun (langkah super-kecil, Preview tiap langkah):**
  1. Latar **`Rumput`** (Tiled) + **`Petualang`** (behavior **Top-down**). → *Preview: bisa jalan.*
  2. Taruh **1 `Telur`**. Beri **variabel objek**: `fiil` = `"نَصَرَ - يَنْصُرُ"`, `benar` = `1`.
  3. Buat teks & tombol (sembunyikan dulu): **`TeksSoal`**, **`TombolYa`**, **`TombolTidak`**, **`TeksHasil`**.
  4. **Aturan 1** — *JIKA `Petualang` sentuh `Telur` MAKA* `TeksSoal` = `Telur.fiil`; simpan variabel
     `Kunci` = `Telur.benar`; tampilkan tombol; sembunyikan telur.
  5. **Aturan 2** — *JIKA klik `TombolYa` MAKA* (sub) *JIKA `Kunci` = 1* → `TeksHasil` "Benar!"; (sub)
     *JIKA `Kunci` = 0* → "Salah". Sembunyikan tombol.
  6. **Aturan 3** — *JIKA klik `TombolTidak` MAKA* kebalikannya (`Kunci`=0 → "Benar!"; `Kunci`=1 → "Salah").
  7. Tambah **2 telur lagi** dengan `fiil`/`benar` berbeda (satu masuk wazan → `benar`=1, satu tidak → 0).
- **Peran:** 🎨 aset & rekam "Benar/Salah" & uji; 🧩 taruh objek + beri variabel objek tiap telur;
  ⚙️ (kamu dulu) tiga aturan itu, sambil **membacakannya keras-keras** ke anak.
- **Tanda paham:** sentuh telur → fi'il muncul → jawab → benar/salah. **Sudah jadi game!** (sengaja
  tanpa `Status`, daftar, menu, atau menang.)

> Inilah "paling sederhana": **3 aturan**, satu scene. Sesi berikutnya menambah **satu** hal saja tiap kali.

### Sesi 3 — Tambah skor & lebih banyak telur (teknik: pel. 4)
- **Tumbuh dari Nano:** tambah teks **`TeksSkor`** "0" + variabel **`Skor`**; di cabang **Benar**,
  tambah satu aksi `Skor` +1 & perbarui teks. Sebar beberapa telur (tiap telur `fiil`/`benar` sendiri).
- **Peran:** 🧩 HUD skor; ⚙️ tambah 1 aksi `Skor +1`; 🎨 uji & sumbang fi'il baru.
- **Tanda paham:** jawaban benar menaikkan skor; ada beberapa telur berbeda.

### Sesi 4 — Rapikan dengan "lampu lalu lintas" `Status` (teknik: pel. 15)
- **Kenapa (biar terasa perlu):** saat soal muncul, petualang **masih bisa jalan & menyentuh telur
  lain** → berantakan. Kita pasang penjaga.
- **Tumbuh:** variabel **`Status`** ("jalan"/"soal"). Beri event **gerak & sentuh-telur** penjaga
  `Status`="jalan"; saat telur disentuh → `Status`="soal"; sesudah menjawab → kembali `"jalan"`.
- **Peran:** ⚙️ `Status` + penjaga (mulai libatkan anak yang penasaran); 🎨 uji "gerak berhenti saat soal?".
- **Tanda paham:** saat soal muncul petualang berhenti; setelah menjawab bisa jalan lagi. **Konsep
  terpenting** (state machine) — dan sekarang mereka paham *kenapa* dibutuhkan.

### Sesi 5 — (opsional/lanjut) Fi'il ACAK dari daftar (teknik: pel. 16)
- **Kapan:** kalau anak sudah nyaman. **Boleh dilewati dulu** — Nano + skor + `Status` sudah game yang bagus.
- **Kenapa:** daripada menaruh fi'il di tiap telur satu-satu, simpan **daftar** & ambil **acak**.
- **Tumbuh:** variabel global **`Soal`** (6 fi'il, Bagian 5b) + `BabTarget`. Saat telur disentuh:
  `SoalIdx = Random(VariableChildCount(Soal) - 1)`; isi `TeksSoal` dari `Soal[SoalIdx]`; ganti
  `Kunci` dengan pembanding: `Soal[SoalIdx].bab` = `BabTarget` → benar, selain itu salah.
- **Tanda paham:** fi'il berganti-ganti sendiri, tak perlu diisi per telur.

### Sesi 6 — Menu pilih wazan (teknik: pel. 12, 13)
- **Tumbuh:** scene **`Menu`** dengan 2 `TombolBab` (**variabel objek** `bab` = 1 & 2) + label wazan;
  klik → `BabTarget = TombolBab.bab` → pindah scene ke hutan.
- **Peran:** ⚙️ event tombol + pindah scene; 🧩 tata scene Menu; 🎨 aset tombol & uji.
- **Tanda paham:** pilih wazan dulu, baru main; pilihan mengubah jawaban yang benar.

### Sesi 7 — Layar Menang (teknik: pel. 6, 12)
- **Tumbuh:** scene **`Menang`**: *JIKA `Skor` ≥ target MAKA pindah ke `Menang`* (teks "Hebat!" +
  tombol "Main lagi" → `Menu`).
- **Peran:** ⚙️ event menang; 🧩 tata scene Menang; 🎨 aset & uji alur.
- **Tanda paham:** kumpulkan cukup → Menang → kembali ke Menu. **Sekarang jadi "Telur Wazan Mini" utuh.**

### Sesi 8 — Bandingkan dengan yang asli & poles (`TUTORIAL.md`)
- **Bersama:** buka `game.json` asli. Temukan tiap bagian mini di sana ("ini yang kita buat!"), lalu
  lihat yang **ditambahkan**: peta acak, kepala terpisah, telur terbang (Tween), boneka + simpan
  (Storage), adegan salah bertahap. Ganti aset/suara mini dengan karya mereka; baca satu event
  bersarang asli.
- **Peran:** 🎨 pasang aset/suara mereka & bermain; 🧩 temukan variabel & ubah teks; ⚙️ telusuri grup
  "Buat peta acak", ubah satu angka (Tween/Storage cukup **didemokan**).
- **Tanda paham:** menunjuk fitur asli dan berkata *"ini versi besar dari punya kita; yang baru cuma
  peta acak, boneka, dan animasi terbang."*

> Lanjutan: perbanyak fi'il, lalu tambahkan satu-per-satu fitur penuh mengikuti `TUTORIAL.md`
> Bagian 8–11 (peta acak → tween → koleksi).

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
