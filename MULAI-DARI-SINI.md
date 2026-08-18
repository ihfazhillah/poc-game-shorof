# Mulai dari Sini — Kursus GDevelop Bertahap (menuju paham Telur Wazan)

Ini **kursus langkah-demi-langkah**. Kita membangun satu game kecil dari nol dan
menumbuhkannya sedikit demi sedikit. **Setiap pelajaran menambahkan satu konsep** yang juga
dipakai di Telur Wazan. Kalau kamu selesaikan semua, kamu praktis sudah membangun "Telur
Wazan mini" — sehingga membaca game aslinya nanti terasa mudah.

Tiap pelajaran punya kotak **➜ Di Telur Wazan** yang menunjukkan di mana konsep itu dipakai.

> **Aturan emas (ajarkan ke anak juga):** ubah **satu** hal → tekan **Preview (▶)** → lihat
> apa yang berubah. Kalau rusak, kamu tahu persis penyebabnya. Rayakan error — itu momen belajar.

## Peta kursus (centang saat selesai)

**Level 0 — Item JIKA (kondisi) & MAKA (aksi) GDevelop + bersarang (paling penting)**
- [ ] 0.1 Anatomi satu Event (JIKA · MAKA · sub-event)
- [ ] 0.2 Kamus item **JIKA** (kondisi) yang dipakai Telur Wazan
- [ ] 0.3 Kamus item **MAKA** (aksi) yang dipakai Telur Wazan
- [ ] 0.4 DAN (banyak kondisi) & TIDAK (Invert)
- [ ] 0.5 Bersarang: sub-event (aturan di dalam aturan)
- [ ] 0.6 Membaca event bersarang asli di Telur Wazan

**Level 1 — Game yang bisa dimainkan**
- [ ] 1. Panggung (Scene) & menjalankannya
- [ ] 2. Tokoh yang berjalan (Objek + Behavior)
- [ ] 3. Banyak barang (Instance)
- [ ] 4. Papan skor (Variabel + Teks)
- [ ] 5. Aturan pertama: JIKA sentuh MAKA skor+1 (Event)
- [ ] 6. Menang (bandingkan variabel, Show/Hide)

**Level 2 — Terasa hidup**
- [ ] 7. Animasi (diam / jalan)
- [ ] 8. Kepala mengikuti badan (dua objek, tiap frame)
- [ ] 9. Suara (dan: anak merekam sendiri)
- [ ] 10. Kamera mengikuti + layer UI

**Level 3 — Menu & interaksi**
- [ ] 11. Tombol yang diklik
- [ ] 12. Pindah antar-scene (Menu → Main)
- [ ] 13. Variabel objek (tiap tombol bawa angkanya sendiri)
- [ ] 14. Timer (pesan yang muncul sebentar)

**Level 4 — "Otak" game (inti Telur Wazan)**
- [ ] 15. Mode permainan: variabel `Status` (state machine)
- [ ] 16. Daftar & acak: array + structure (seperti daftar soal)
- [ ] 17. Perulangan: Repeat & For Each (menyebar barang otomatis)
- [ ] 18. Peta petak dari kode (procedural, versi mini)
- [ ] 19. Tween (barang terbang ke keranjang)
- [ ] 20. Menyimpan skor (Storage) — seperti koleksi boneka

---

# LEVEL 0 — Item JIKA (kondisi) & MAKA (aksi) GDevelop + bersarang

Ini bagian **paling penting** untuk memahami alur Telur Wazan. Di GDevelop, satu aturan disebut
**Event**, dan tiap Event punya tiga bagian:

- **JIKA** = daftar **Conditions** (kondisi/syarat yang dicek).
- **MAKA** = daftar **Actions** (aksi yang dijalankan kalau semua syarat benar).
- **Sub-events** = aturan **bersarang** di dalamnya (dijalankan hanya kalau JIKA induk benar).

Di sini kita **kenali item-item JIKA & MAKA yang benar-benar dipakai Telur Wazan**, lalu belajar
**membaca sarangnya**. Semua nama di bawah persis seperti yang kamu lihat saat menekan
*Add condition* / *Add action* di GDevelop (nama bisa sedikit beda antar-versi).

## 0.1 Anatomi satu Event (contoh nyata dari Telur Wazan)

Event "klik tombol wazan" di scene `Menu` dibaca begini (menjorok = bagian di dalam):

```
● EVENT
  JIKA (Conditions):
    • Kursor/sentuhan ada di atas objek  →  TombolBab
    • Tombol mouse dilepas               →  "Left"
  MAKA (Actions):
    • Ubah variabel angka   →  BabTarget = TombolBab.bab
    • Mainkan suara         →  audio/sfx/klik.wav
    • Pindah ke scene       →  "Hutan"
```

Dua kondisi ditumpuk = keduanya harus benar (**DAN**). Kalau salah satu tidak, MAKA-nya tak jalan.

> **Ajak anak:** biasakan **membaca event keras-keras**: *"JIKA kursor di tombol DAN mouse
> dilepas, MAKA simpan pilihan, bunyi klik, pindah ke Hutan."* Kemampuan **membaca** event ini
> lebih penting daripada menghafal nama menunya.

## 0.2 Kamus item JIKA (kondisi) yang dipakai Telur Wazan

Inilah "kosakata syarat" game ini. (Kolom terakhir: pelajaran tempat kita pakai/pelajari.)

| Item JIKA (nama di GDevelop) | Artinya (dicek benar/salah) | Contoh nyata di Telur Wazan | Pelajaran |
|---|---|---|---|
| **At the beginning of the scene** | benar **sekali** saat scene mulai | menyiapkan skor, membuat peta | 6, 17 |
| **The cursor/touch is on an object** | kursor di atas objek itu | di atas `TombolBab`, `TombolYa` | 11 |
| **Mouse button released** | tombol mouse dilepas | klik "Left" | 11 |
| **Collision** (hitboxes) | dua objek bersentuhan | `Petualang` × `Telur` / `Pohon` / `TandaFinish` | 5 |
| **Compare the text of a variable** | isi variabel **teks** sama/tidak | `Status = "jalan"` | 15 |
| **Compare number variable** | bandingkan variabel **angka** | `Skor >= TargetTelur`, `Soal[SoalIdx].bab = BabTarget` | 4, 16 |
| **Compare object variable** (number) | variabel **objek** pada instance | `PetaTelur.sel = Telur.sel` | 13 |
| **Compare two numbers** | bandingkan dua **ekspresi** angka | jarak sel telur dari START `> 3` | 18 |
| **Is moving** (Top-down) | objek sedang bergerak | `Petualang` jalan → animasi `jalan` | 7 |
| **Current animation is** | animasi objek sedang apa | `Telur` animasi = `pecah` | 7 |
| **Animation finished** | animasi non-loop selesai | `Asap` selesai → dihapus | 7 |
| **Key pressed** (teks) | tombol keyboard ditekan | `"w"`,`"a"`,`"s"`,`"d"` | 2 |
| **Value of a scene timer** | umur timer > sekian detik | `salah > 0.8`, `hasil > LamaHasil` | 14 |
| **Trigger once while true** | benar **hanya di frame pertama** | pesan "telur kurang" muncul sekali | 6 |
| **Tween finished** | animasi tween selesai | telur sampai keranjang → "ding" | 19 |
| **Storage: Group exists** | ada data tersimpan | cek simpanan `"TelurWazan"` sebelum dimuat | 20 |
| **Invert** (centang di kondisi) | membalik jadi **TIDAK** | *TIDAK* sedang bergerak → animasi `diam` | 7 |

## 0.3 Kamus item MAKA (aksi) yang dipakai Telur Wazan

"Kosakata tindakan" game ini:

| Item MAKA (nama di GDevelop) | Melakukan apa | Contoh nyata di Telur Wazan | Pelajaran |
|---|---|---|---|
| **Change number variable** | ubah variabel angka (=,+,−) | `Skor + 1`, `BabTarget = ...` | 4 |
| **Change text variable** | ubah variabel teks | `Status = "soal"` | 15 |
| **Modify the text** (Text object) | ganti tulisan objek teks | `TeksSkor = ToString(Skor)+" / "+...` | 4 |
| **Change color / Set padding** (Text) | warna & ruang teks | padding agar harakat Arab tak terpotong | 9 |
| **Show / Hide** | tampil / sembunyikan objek | sembunyikan `GrupSoal`, tampilkan panel | 6 |
| **Set the animation name** | ganti animasi objek | `Petualang → "telur"`, kepala `"kaget"` | 7 |
| **Create an object** | buat objek baru saat main | buat `Telur`, `Pohon`, `Asap` | 17 |
| **Delete an object** | hapus objek | telur yang sudah dijawab | 5 |
| **Set position / X / Y / center** | pindahkan objek | kepala menempel badan; taruh START/FINISH | 8 |
| **Play a sound / on a channel** | bunyikan suara | klik, pecah, "Benar!", "Salah!" | 9 |
| **Change to another scene** | pindah scene | `Menu → Hutan → Menang` | 12 |
| **Center the camera on an object** | kamera mengikuti | mengikuti `Petualang` | 10 |
| **Separate objects** | dorong keluar dari tabrakan | `Petualang` didorong dari `Pohon` (penghalang) | — |
| **Reset a scene timer** | mulai ulang hitungan waktu | timer `salah`, `hasil`, `info` | 14 |
| **Add value to array / Change `Peta[..]`** | isi elemen array | membangun grid peta | 16, 18 |
| **Add position/scale tween** | animasi gerak/skala halus | telur→keranjang, boneka→rak | 19 |
| **Storage: Write / Read a text** | simpan / muat data perangkat | `ToJSON(Koleksi)` ke `"TelurWazan"` | 20 |
| **Simulate press … key** (Top-down) | pura-pura tekan tombol | WASD menggerakkan `Petualang` | 2 |

> Tak perlu menghafal tabel ini. Gunakan sebagai **kamus**: saat membaca sebuah event di Telur
> Wazan, cari nama itemnya di sini untuk tahu artinya.

## 0.4 DAN (banyak kondisi) & TIDAK (Invert)

- **Menumpuk beberapa kondisi dalam satu event = DAN** — semua harus benar. Contoh Telur Wazan:
  `JIKA Status = "jalan"` **DAN** `Collision Petualang–Telur` MAKA telur pecah. (Kondisi `Status`
  ini adalah **penjaga** — tanpa itu, telur bisa pecah saat panel soal sedang tampil.)
- **TIDAK** = centang **Invert** pada sebuah kondisi. Contoh: `JIKA Petualang TIDAK bergerak
  MAKA animasi "diam"`.

## 0.5 Bersarang: sub-event (aturan di dalam aturan)

**Konsep inti kedua.** Sebuah event bisa punya **sub-event** — aturan yang **menjorok ke dalam**
di bawahnya. Aturannya:

1. Sub-event **hanya diperiksa jika JIKA induknya benar** lebih dulu.
2. Objek yang sudah "dipilih" kondisi induk **diteruskan** ke sub-event (mis. jika induk memilih
   satu `Telur` tertentu lewat collision, sub-event bekerja pada telur itu).
3. Berguna untuk **beberapa langkah berurutan**, atau **memutuskan sesuatu setelah mengulang**.

Bentuknya (menjorok = di dalam):

```
● JIKA (induk)
  MAKA (aksi induk)
    ● JIKA (sub-event 1)   ← dicek hanya kalau induk benar
      MAKA ...
    ● JIKA (sub-event 2)
      MAKA ...
```

## 0.6 Membaca event bersarang asli di Telur Wazan

Buka scene **Hutan → Events**, temukan tiga contoh ini dan baca strukturnya:

**Contoh A — Menemukan telur (induk) lalu memilih soal (sarang):**

```
● JIKA Status = "jalan"  DAN  Collision Petualang–Telur
  MAKA  Status = "soal";  Telur animasi "pecah";  kepala "kaget";  MauYa = Random(1)
    ● Repeat 30 kali   (sub-event: ulang sampai dapat soal yang cocok)
        ● JIKA MauYa = 1  DAN  Soal[SoalIdx].bab = BabTarget   MAKA Ketemu = 1
        ● JIKA MauYa = 0  DAN  Soal[SoalIdx].bab ≠ BabTarget   MAKA Ketemu = 1
    ● JIKA Soal[SoalIdx].bab = BabTarget  MAKA Kunci = "ya"
    ● (lalu) isi teks panel dari Soal[SoalIdx]
```

Perhatikan **tiga tingkat**: event collision (induk) → `Repeat` (sub) → dua JIKA pengecek (sub
dari `Repeat`). Inilah "aturan di dalam aturan di dalam aturan".

**Contoh B — Menjawab (satu induk, banyak cabang bersarang):**

```
● JIKA Status = "soal"  DAN  Jawaban ≠ ""     (sudah menjawab)
  MAKA sembunyikan panel soal
    ● JIKA Jawaban = Kunci     MAKA benar: Skor+1, telur terbang ke keranjang (tween)
    ● JIKA Jawaban ≠ Kunci     MAKA salah: mulai adegan (Status = "salah")
```

Induk memastikan "sudah ada jawaban", lalu **dua sub-event** memisahkan jalur benar vs salah.

**Contoh C — Peta acak (perulangan bersarang):**

```
● At the beginning of the scene
    ● Repeat 4 kali   (menyambung titik jalur)
        ● Repeat (mendatar)  → set Peta[...] = 1
        ● Repeat (menegak)   → set Peta[...] = 1
```

`Repeat` di dalam `Repeat` — cara membuat jalur berbentuk L. (Detailnya di Pelajaran 18.)

> **Latihan membaca (untuk anak & kamu):** tunjuk satu event di Hutan, lalu ucapkan:
> *"JIKA … MAKA …, dan di dalamnya ada aturan lain yang berbunyi …"*. Kalau bisa membacakan
> alurnya, berarti sudah paham. **Membaca dulu, baru menulis.**

Mulai Level 1, tiap pelajaran adalah **satu Event nyata yang kamu tulis sendiri** — sebutkan
selalu "JIKA apa, MAKA apa, ada sarang tidak?" sebelum mengekliknya.

---

# LEVEL 1 — Game yang bisa dimainkan

## 1. Panggung (Scene) & menjalankannya

**Tujuan:** kenal *Scene* dan tombol *Preview*.

1. GDevelop → **Create a new project** → **Empty game** → pilih folder → **Create**.
2. Sudah ada satu scene (mis. "NewScene"). Klik dua kali untuk membukanya.
3. Tekan **Preview (▶)**. Muncul jendela kosong. Tutup lagi.

**➜ Di Telur Wazan:** ada 4 scene — `Menu`, `Hutan`, `Menang`, `Koleksi`. Kamu baru punya 1.

---

## 2. Tokoh yang berjalan (Objek + Behavior)

**Tujuan:** *Objek* dan *Behavior* (perilaku siap pakai).

1. Di panggung: **Add a new object** → **Sprite**.
2. **Add animation** → tambahkan satu gambar (apa saja; boleh gambar buatan anak). Namai objek
   **`Tokoh`** → **Apply**.
3. Drag `Tokoh` ke tengah panggung.
4. Klik `Tokoh` → panel kanan **Behaviors** → **Add behavior** → cari **Top-down movement** → tambah.
5. **Preview** → tokoh **sudah bisa jalan pakai tombol panah**, tanpa menulis kode!

**➜ Di Telur Wazan:** objek `Petualang` memakai **Top-down movement** yang sama. (Kecepatannya
diatur di properti behavior — coba ubah *Max speed*.)

> **Ajak anak:** "Gerakkan dia!" Perasaan bisa mengendalikan tokoh = motivasi pertama.

---

## 3. Banyak barang (Instance)

**Tujuan:** beda *Objek* (cetakan) vs *Instance* (salinan di panggung).

1. **Add a new object** → **Sprite** → gambar bintang → namai **`Bintang`** → Apply.
2. Drag ke panggung. Lalu **Ctrl+C, Ctrl+V** beberapa kali → taruh **3 bintang** di tempat berbeda.

Sekarang: **1 objek** `Bintang`, **3 instance** di panggung.

**➜ Di Telur Wazan:** `Telur` juga satu objek, disebar jadi banyak — bedanya di sana
penyebarannya otomatis lewat event (Pelajaran 17–18).

---

## 4. Papan skor (Variabel + Teks)

**Tujuan:** *Variabel* (kotak angka) dan objek *Teks*.

1. **Add a new object** → **Text** → isi `Skor: 0` → namai **`TeksSkor`** → Apply. Taruh di pojok.
2. Buat variabel scene: buka **Scene variables** (ikon variabel di toolbar scene, atau menu
   scene) → **Add** → nama **`Skor`**, tipe **Number**, nilai **0**.

**➜ Di Telur Wazan:** ada variabel `Skor` dan teks `TeksSkor` (menampilkan `0 / 5`).

---

## 5. Aturan pertama: JIKA sentuh MAKA skor+1 (Event)

**Tujuan:** inti segalanya — *Event* **JIKA (kondisi) MAKA (aksi)**.

Buka tab **Events** (di atas panggung) → **Add a new event**.

1. **Add condition** → klik **`Tokoh`** → **Collision** → objek **`Bintang`**.
   *(JIKA Tokoh menyentuh Bintang…)*
2. **Add action** → **`Bintang`** → **Delete object**. *(…MAKA hapus bintang itu)*
3. **Add action** → **Variables** → **Change number variable** → `Skor`, operasi **+**, nilai **1**.
4. **Add action** → **`TeksSkor`** → **Modify the text** → isi: `"Skor: " + ToString(Skor)`

**Preview.** Jalan ke bintang → hilang, skor naik. 🎉

**➜ Di Telur Wazan:** aturan intinya sama — *JIKA `Petualang` collision `Telur`* — hanya
"MAKA"-nya lebih ramai (telur pecah → tampil soal). `ToString(...)` juga dipakai untuk menyusun
teks `0 / 5`.

> **Ajak anak:** baca keras: "**JIKA** kena bintang, **MAKA** bintang hilang, skor tambah satu."

---

## 6. Menang (bandingkan variabel, Show/Hide)

**Tujuan:** *kondisi angka* dan menyembunyikan/menampilkan objek.

1. **Add a new object** → **Text** → isi `MENANG!` → namai **`TeksMenang`** → Apply, taruh di tengah.
2. **Event baru:** condition **Variables → Compare number variable** → `Skor` **≥** `3`;
   action **`TeksMenang` → Show**.
3. Agar tersembunyi di awal: **event baru** dengan condition **At the beginning of the scene**
   → action **`TeksMenang` → Hide**. (Taruh event ini paling atas.)

**Preview.** Kumpulkan 3 bintang → muncul **MENANG!**

**➜ Di Telur Wazan:** "JIKA skor cukup MAKA menang" persis begini — hanya ditambah syarat
**sampai FINISH**, lalu **pindah ke scene `Menang`**.

✅ **Level 1 selesai:** kamu sudah membuat game utuh (jalan, kumpulkan, menang).

---

# LEVEL 2 — Terasa hidup

## 7. Animasi (diam / jalan)

**Tujuan:** satu objek punya banyak *animasi*, ganti sesuai keadaan.

1. Klik dua kali objek `Tokoh`. Kamu punya animasi pertama — namai **`diam`**.
2. **Add animation** kedua, namai **`jalan`**, isi 2–4 gambar (kaki bergerak). Apply.
3. Tab **Events**, tambah 2 event:
   - condition **`Tokoh` → Top-down → Is moving**; action **`Tokoh` → Set the animation name → `"jalan"`**.
   - condition **Is moving** (klik **Invert** jadi *tidak* bergerak); action **Set the animation name → `"diam"`**.

**Preview.** Diam vs jalan berganti sendiri.

**➜ Di Telur Wazan:** `Petualang` punya animasi `diam`, `jalan`, `telur`; Telur punya `utuh`
& `pecah`; kepala punya `normal` & `kaget`. Persis pola ini.

---

## 8. Kepala mengikuti badan (dua objek, tiap frame)

**Tujuan:** satu event tanpa kondisi = berjalan **tiap frame**; objek menempel objek lain.

1. **Add a new object** → **Sprite** → gambar wajah → namai **`Kepala`** → taruh dekat Tokoh.
2. **Event baru tanpa kondisi** (biarkan kondisi kosong), tambah 2 aksi:
   - **`Kepala` → Position → Set X** = `Tokoh.X()` (atau `Tokoh.X() + 4` untuk menggeser).
   - **`Kepala` → Position → Set Y** = `Tokoh.Y() - 50`.

**Preview.** Kepala selalu menempel di atas badan, ke mana pun berjalan.

**➜ Di Telur Wazan:** persis event "Kepala mengikuti badan" (`KepalaPetualang.X = Petualang.X()+4`,
`Y = Petualang.Y()-50`). Kepala dipisah supaya ekspresinya (`normal`/`kaget`) bisa ganti sendiri.

> **Catatan:** event tanpa kondisi = MAKA-nya dijalankan **±60×/detik**. Itu sebabnya kepala
> selalu pas mengikuti.

---

## 9. Suara (dan: anak merekam sendiri)

**Tujuan:** memutar suara dari event. **Di Telur Wazan, suara diisi rekaman anak, bukan mesin.**

1. Rekam suara (HP/laptop), simpan sebagai **mp3/wav** (mis. `dapat.mp3`).
2. GDevelop: **Project manager → Resources → Add** → pilih file itu.
3. Di event **collision Bintang** (Pelajaran 5), tambah action **Audio → Play a sound** → pilih `dapat.mp3`.

**Preview.** Tiap dapat bintang → terdengar suara anak.

**➜ Di Telur Wazan:** ada banyak file di `audio/` (benar/salah/menang + bacaan tiap fi'il).
Untuk mengganti, timpa file dengan **nama sama**, atau tambah baru lewat *Resources* seperti di atas.

> **Ajak anak:** bagi peran — narator, "kelinci" lucu, pembaca fi'il Arab. Merekam suara sendiri
> membuat game terasa milik mereka.

---

## 10. Kamera mengikuti + layer UI

**Tujuan:** dunia lebih besar dari layar (kamera mengikuti); HUD tidak ikut bergeser (*layer* UI).

1. Perbesar area: taruh bintang jauh-jauh sehingga melebihi layar.
2. **Event tanpa kondisi** → action **Layers and cameras → Center the camera on an object** → `Tokoh`.
   **Preview** → kamera mengikuti tokoh.
3. Buat layer UI: panel **Layers** (di editor scene) → **Add a layer** → namai **`UI`**.
4. Pindahkan `TeksSkor` ke layer `UI` (pilih instance → properti **Layer** = `UI`).

**Preview.** Tokoh berjalan, kamera ikut, tapi skor **diam** di pojok.

**➜ Di Telur Wazan:** dunia `Hutan` 2000×1400 (lebih besar dari layar), kamera mengikuti dan
di-*clamp* pada batas; semua HUD, panel soal, dan peta mini ada di layer **`UI`**.

✅ **Level 2 selesai:** game-mu sekarang terasa hidup.

---

# LEVEL 3 — Menu & interaksi

## 11. Tombol yang diklik

**Tujuan:** merespons klik mouse pada objek.

1. **Add a new object** → **Sprite** → gambar tombol → namai **`TombolMulai`** → taruh di layar.
2. **Event baru:** conditions **`TombolMulai` → The cursor/touch is on the object** **DAN**
   **Mouse/touch → Mouse button released → Left**; action **Audio → Play a sound** (bunyi klik) —
   nanti kita ganti aksinya jadi pindah scene.

**Preview.** Klik tombol → bunyi.

**➜ Di Telur Wazan:** 6 tombol wazan & tombol Rak memakai pola **cursor on object + klik kiri
dilepas** ini.

---

## 12. Pindah antar-scene (Menu → Main)

**Tujuan:** banyak scene dan berpindah di antaranya.

1. **Project manager → Scenes → Add a scene** → namai **`Menu`**. Taruh `TombolMulai` di scene
   `Menu` (dan judul teks kalau mau).
2. Jadikan `Menu` scene pertama: klik kanan `Menu` → **Set as start scene** (atau atur di
   properti game).
3. Di scene `Menu`, event tombol (Pelajaran 11): ganti/ tambah action **Scene → Change to another
   scene** → pilih scene game utamamu.

**Preview.** Mulai di `Menu` → klik tombol → masuk ke game.

**➜ Di Telur Wazan:** `Menu` → (klik wazan) → `Hutan` → `Menang` → `Koleksi`, semuanya lewat
**Change scene**. Scene pertama diatur lewat `firstLayout` = `Menu`.

---

## 13. Variabel objek (tiap tombol bawa angkanya sendiri)

**Tujuan:** *variabel objek* — tiap instance menyimpan datanya sendiri.

1. Di scene `Menu`, buat objek `TombolMulai` jadi beberapa (mis. 3 instance).
2. Klik instance pertama → properti **Instance variables → Add** → nama **`nomor`** = `1`.
   Instance kedua `nomor`=`2`, ketiga `nomor`=`3`.
3. Buat variabel global **`Pilihan`** (Project manager → Global variables).
4. Event klik tombol: action **Change number variable `Pilihan` = `TombolMulai.nomor`**.
   Satu event menangani **semua** tombol karena tiap instance membawa `nomor` sendiri.

**➜ Di Telur Wazan:** tiap `TombolBab` (dan `LabelBab`) membawa variabel objek **`bab`** (1–6);
saat diklik: `BabTarget = TombolBab.bab`. Persis ini.

> **Ajak anak:** "Tiap tombol punya nomornya sendiri di sakunya." Klik tombol 3 → papan ingat 3.

---

## 14. Timer (pesan yang muncul sebentar)

**Tujuan:** waktu — menampilkan sesuatu selama beberapa detik.

1. Saat ingin memulai hitungan (mis. di event menang), action **Timers → Reset a scene timer**
   → nama **`pesan`**; lalu **Show** sebuah teks.
2. **Event baru:** condition **Timers → Value of a scene timer** `pesan` **>** `2`; action
   **Hide** teks itu.

**➜ Di Telur Wazan:** timer dipakai untuk pesan "telur kurang" (timer `info`), lama panel hasil
(`hasil`), dan **adegan bertahap saat salah** (timer `salah`: 0,8s → 1,8s → 6s).

---

# LEVEL 4 — "Otak" game (inti Telur Wazan)

## 15. Mode permainan: variabel `Status` (state machine)

**Tujuan:** satu variabel teks menyetir "mode", tiap event dijaga oleh mode itu.

1. Variabel scene **`Status`** (Text) = `"main"`.
2. Beri **semua** event gameplay (gerak, collision) kondisi tambahan **Compare the text of a
   variable `Status` = `"main"`**.
3. Saat sesuatu terjadi (mis. dapat bintang khusus), set `Status = "jeda"`. Selama `Status`
   bukan `"main"`, event gameplay berhenti sendiri.

**➜ Di Telur Wazan:** `Status` berpindah `jalan → soal → hasil / salah → tanya_ulang`. Hampir
setiap event diawali `JIKA Status = "..."`. Analogi lampu lalu lintas: `jalan`=hijau,
`soal`=merah (berhenti, jawab dulu).

> Ini konsep **state machine** — paling penting untuk memahami scene `Hutan`.

---

## 16. Daftar & acak: array + structure (seperti daftar soal)

**Tujuan:** menyimpan **daftar** data dan mengambil **acak** — dasar sistem soal.

1. Variabel global **`Daftar`**, tipe **Array**. Tambah beberapa **child** bertipe **Structure**,
   tiap structure punya anak, mis. `teks` (Text) dan `benar` (Number 0/1).
2. Ambil item acak: action **Change number variable `Idx` = `Random(VariableChildCount(Daftar) - 1)`**.
3. Pakai isinya: `Daftar[Idx].teks` (untuk teks), `Daftar[Idx].benar` (untuk cek).

**➜ Di Telur Wazan:** variabel `Soal` adalah **array 81 structure** (`madhi`, `mudhari`, `arti`,
`bab`, `suara`). Saat telur pecah, `SoalIdx = Random(VariableChildCount(Soal) - 1)`, lalu diulang
sampai jawabannya seimbang (±50% "ya"). Nilai dibaca dengan `Soal[SoalIdx].madhi`, dst.

---

## 17. Perulangan: Repeat & For Each (menyebar barang otomatis)

**Tujuan:** membuat banyak objek dengan kode, bukan tangan.

1. Di **At the beginning of the scene**, tambah sub-event **Repeat** `5` kali → action
   **Create object `Bintang`** di posisi acak: X = `RandomInRange(0, 1200)`, Y = `RandomInRange(0, 600)`.
2. **For Each object** `Bintang` → lakukan sesuatu ke tiap bintang (mis. atur ukuran).

**Preview.** 5 bintang muncul di tempat acak tiap main.

**➜ Di Telur Wazan:** telur, pohon, bunga, dan sel peta mini semuanya **dibuat oleh Repeat**
saat scene mulai; `For Each` dipakai mengisi label/rak. Itu sebabnya scene `Hutan` tampak kosong
di editor — isinya lahir saat Preview.

---

## 18. Peta petak dari kode (procedural, versi mini)

**Tujuan:** memahami peta acak Telur Wazan lewat versi kecil.

1. Variabel scene **`Peta`** (Array). Di awal scene, **Repeat 20** → **Push number 0 to `Peta`**
   (bayangkan 20 petak, semua "kosong").
2. **Repeat 20** dengan penghitung `I` (naikkan `I` tiap putaran): condition
   **`Peta[I]` = `0`** → **Create `Bintang`** di `I * 60`, `200`. (Menaruh objek per-petak.)

Kamu baru membuat "dunia" dari sebuah **array angka** — persis ide peta Telur Wazan, hanya 1 baris.

**➜ Di Telur Wazan:** `Peta` adalah array **20×14 = 280** angka (`0`=pohon, `1`=jalur, `2`=jalur+telur),
indeks sel = `baris*20 + kolom`. Jalur digambar bentuk huruf L dari START ke FINISH, sisanya pohon.
Baca grup event **"Buat peta acak"** — komentarnya sudah berbahasa Indonesia.

> Tak perlu paham semua matematikanya. Cukup rasakan: **array angka + perulangan → dunia**.

---

## 19. Tween (barang terbang ke keranjang)

**Tujuan:** animasi gerak halus tanpa menghitung tiap frame.

1. Klik objek `Bintang` → **Behaviors → Add → Tween**.
2. Di event dapat bintang, ganti "Delete" dengan: action **Tween → Add object position tween** →
   target = posisi pojok skor, durasi `0.8` detik, easing `easeInQuad`.
3. **Event baru:** condition **Tween → Tween finished**; action **Delete** bintang + bunyi "ding".

**➜ Di Telur Wazan:** saat jawaban benar, `TelurTerbang` **tween** ke `Keranjang` (0,8s), lalu
keranjang membesar sebentar (tween skala). Boneka juga tween terbang ke rak di scene `Menang`.

---

## 20. Menyimpan skor (Storage) — seperti koleksi boneka

**Tujuan:** menyimpan data agar **tidak hilang** saat game ditutup.

1. Saat menang, action **Storage → Write a text in storage**: nama grup `"GameBintang"`,
   elemen `"skor"`, nilai `ToString(Skor)` (atau `ToJSON(Daftar)` untuk data kompleks).
2. Di **awal scene**, condition **Storage → Group exists** `"GameBintang"`; action
   **Storage → Read a text from storage** → simpan ke variabel → tampilkan.

**Preview**, menang, tutup game, buka lagi → skor tetap ada.

**➜ Di Telur Wazan:** scene `Menang` menyimpan `ToJSON(Koleksi)` ke penyimpanan `"TelurWazan"`;
scene `Menu` & `Koleksi` memuatnya kembali. Itulah kenapa rak boneka tak hilang antar-sesi.

*(Bonus opsional — Pelajaran 21: blok **JavaScript**. Di Telur Wazan ada satu blok JS kecil, hanya
untuk memutar suara yang **nama filenya diambil dari variabel** — karena aksi "Play a sound" biasa
tak bisa memilih file dari variabel. Aman diabaikan saat belajar.)*

---

# Selesai — kamu sudah melihat semua ide Telur Wazan

Yang barusan kamu bangun memetakan **seluruh** konsep game asli:

| Kamu pelajari | Di Telur Wazan | Bagian di `TUTORIAL.md` |
|---|---|---|
| Scene & Preview | 4 scene | 0–3 |
| Objek + Top-down | `Petualang` | 4 |
| Instance banyak | `Telur` disebar | 8 |
| Variabel + Teks + `ToString` | `Skor`, `TeksSkor` | 6 |
| Collision → aksi | telur pecah → soal | 5, 7 |
| Menang (bandingkan) | menang + FINISH | 7 |
| Animasi | diam/jalan, utuh/pecah | 4 |
| Kepala ikut badan | `KepalaPetualang` | 4 |
| Suara | rekaman anak | 9 |
| Kamera + layer UI | hutan 2000×1400, HUD | 8–9 |
| Tombol klik | 6 tombol wazan | 5, 7 |
| Pindah scene | Menu↔Hutan↔Menang↔Koleksi | 3, 7 |
| Variabel objek | `bab` tiap tombol | 7 |
| Timer | `info`, `hasil`, `salah` | 7, 10 |
| `Status` (state machine) | jalan/soal/hasil/salah | 7 |
| Array + structure + Random | `Soal` (81) | 6, 10 |
| Repeat / For Each | sebar telur/pohon | 8 |
| Peta petak array | peta acak 20×14 | 8 |
| Tween | telur→keranjang, boneka→rak | 10 |
| Storage | koleksi boneka | 10 |

## Lanjut ke sini

➡️ Buka **`TUTORIAL.md`** mulai **Bagian 0**. Semua yang kamu temui di sana sudah pernah kamu
bangun sendiri di sini — tinggal lebih besar dan digabung jadi satu game utuh.

> **Untuk mengajar anak:** kerjakan **satu pelajaran per sesi**, selalu tutup dengan "coba
> ubah satu hal lalu Preview". Biarkan mereka menggambar & merekam suara di pelajaran 2, 3, 7, 9 —
> di situ game mulai terasa milik mereka.
