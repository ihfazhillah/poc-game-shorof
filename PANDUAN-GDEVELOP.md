# Panduan Memahami Proyek "Telur Wazan" di GDevelop

Dokumen ini menjelaskan *isi* proyek supaya bisa dipakai sebagai titik awal belajar GDevelop
dan mengajarkannya ke anak-anak. Bacalah sambil membuka `game.json` di GDevelop.

## 1. Tiga konsep dasar GDevelop yang dipakai

1. **Scene** (layar/adegan). Proyek ini punya 4: `Menu`, `Hutan`, `Menang`, `Koleksi`.
2. **Objek** (gambar/teks yang tampil). Objek bisa punya *behavior* (perilaku bawaan, mis. *Top-down
   movement* = bisa digerakkan dengan panah tanpa menulis apa pun) dan *variabel objek*.
3. **Event** = *"JIKA kondisi, MAKA aksi"*. Semua logika game ditulis dalam bentuk ini di tab
   **Events** tiap scene. Event dijalankan **setiap frame** (±60× per detik) dari atas ke bawah.

Selain itu ada **variabel** (kotak penyimpan angka/teks): variabel *global* (berlaku di semua scene),
variabel *scene*, dan variabel *objek*.

## 2. Peta proyek

```
Project manager
├─ Global objects   : Petualang, KepalaPetualang, Kelinci, KepalaKelinci, Telur, Keranjang, Rumput,
│                     Pohon, Semak, Bunga, Batu, Asap, TandaStart, TandaFinish, Panah, Boneka
├─ Global variables : TargetTelur, JumlahTelurDiHutan, BabTarget, NamaBab[6], Soal[81], Koleksi[6]
└─ Scenes
   ├─ Menu    : judul + 6 tombol wazan (TombolBab & LabelBab, tiap instance punya variabel bab=1..6) + tombol Rak
   ├─ Hutan   : permainan utama; PETA DIBUAT ACAK saat scene mulai (layer "" = hutan, "UI" = HUD & panel)
   ├─ Menang  : kelinci POP jadi boneka -> boneka terbang masuk tombol RAK -> Koleksi[BabTarget-1] + 1 (Storage)
   └─ Koleksi : rak 6 boneka (Boneka, TeksJumlah, LabelWazan; tiap instance punya variabel bab)
```

### Kepala terpisah dari badan
`Petualang` = badan (punya behavior Top-down movement). `KepalaPetualang` = objek lain.
Event *"Kepala mengikuti badan"* menyalin posisi tiap frame:
```
KepalaPetualang.X = Petualang.X() + 4
KepalaPetualang.Y = Petualang.Y() - 50
```
Sama untuk `Kelinci` dan `KepalaKelinci`. Karena terpisah, ekspresi wajah bisa diganti sendiri:
kepala petualang punya animasi `normal` & `kaget`; kepala kelinci `biasa` & `marah`.
Ubah angka +4 / -50 (dan -4 / -62 untuk kelinci) kalau anak menggambar kepala dengan ukuran lain.
Mata semua tokoh digambar sebagai huruf **hamzah (ء)** dengan font Amiri (`tools/buat_aset.py`, fungsi `hamzah`).

### Peta acak (grup event "Buat peta acak" di scene Hutan)
Hutan = grid **20 × 14 sel**, 1 sel = 100 px (variabel scene `Peta`, array 280 angka:
0 = pohon, 1 = jalur, 2 = jalur + telur; indeks sel = baris × 20 + kolom).
1. Semua sel diisi 0.
2. Pilih 5 titik jalur `WX`/`WY`: START di kolom 1, tiga titik acak makin ke kanan (kolom 5–8, 9–12,
   13–16), FINISH di kolom 18. Barisnya acak → jalur berkelok berbeda tiap main.
3. Titik disambung bentuk **huruf L** (mendatar dulu, lalu tegak), lebar 3 sel → sel jalur = 1.
4. Sel yang masih 0 ditanami `Pohon` (digeser acak sedikit supaya alami). Pohon = **penghalang**:
   event *Petualang collision Pohon → Separate objects*.
5. Telur ditaruh di sel jalur acak (nilai 1 → 2) yang tidak dekat START, sebanyak `JumlahTelurDiHutan`.
6. Hiasan bunga; lalu `TandaStart`, `TandaFinish`, dan petualang dipindahkan ke selnya.

Karena semuanya dibuat oleh event, di *scene editor* Hutan hanya terlihat petualang, kelinci, HUD, dan
panel — pohon/telur baru muncul saat Preview. Ini contoh bagus **procedural generation** sederhana.

**Peta mini** (pojok kanan atas, layer UI): saat pohon ditanam, tiap sel juga dibuatkan `PetaSel` kecil
(8×8 px; gelap = pohon, terang = jalur). Telur → titik `PetaTelur` (punya variabel `sel`, dihapus saat
telurnya diambil), START/FINISH → `PetaStart`/`PetaFinish`, dan titik merah `PetaPemain` mengikuti
petualang tiap frame: `x = 1104 + Petualang.CenterX() / 100 * 8`.

## 3. Alur permainan di scene Hutan (mesin keadaan sederhana)

Variabel scene `Status` menyimpan keadaan permainan:

| Status | Artinya | Berpindah ketika |
|---|---|---|
| `"jalan"` | petualang bebas berjalan | menabrak telur → `"soal"` |
| `"soal"` | telur pecah, panel soal tampil, petualang tidak bisa bergerak | klik YA/TIDAK → `"hasil"` |
| `"hasil"` | jawaban BENAR: telur terbang ke keranjang, panel hasil tampil `LamaHasil` detik | timer habis → `"jalan"` (atau ke scene Menang jika `Skor >= TargetTelur`) |
| `"salah"` | adegan bertahap (variabel `TahapSalah` + timer `salah`): 0,8 dtk → POP jadi telur + asap; 1,8 dtk → kelinci datang & marah; 6 dtk → tanya | → `"tanya_ulang"` |
| `"tanya_ulang"` | panel bawah "Mau mulai lagi dari awal?" | YA → scene Hutan diulang (peta baru); TIDAK → Menu |

**Menang** tidak lagi otomatis saat skor cukup: petualang harus **sampai FINISH** (collision dengan
`TandaFinish`). Skor ≥ `TargetTelur` → scene Menang; kurang → pesan "Telur masih kurang N!" (boleh
balik cari telur). Panah kuning di HUD (`Panah`) selalu menunjuk arah FINISH:
`Panah.angle = AngleBetweenPositions(Petualang.X(), Petualang.Y(), TandaFinish.X(), TandaFinish.Y())`.

Hampir setiap event di Hutan diawali kondisi `Status = "..."` — ini kunci supaya event tidak
"bertabrakan". Pola ini sangat berguna untuk game apa pun.

## 4. Event-event penting (urutan di tab Events scene Hutan)

1. **Saat mulai** – reset skor, sembunyikan panel & kelinci, isi teks HUD, sebar telur
   (`Repeat JumlahTelurDiHutan` × *Create Telur* di posisi acak).
2. **Kepala mengikuti badan** – lihat di atas.
3. **Kontrol tambahan WASD** – *Simulate key press* pada behavior Top-down movement.
4. **Animasi petualang** – *Is moving* → animasi `jalan`, kalau tidak → `diam`.
5. **Kamera, batas hutan, pohon penghalang, panah** – `clamp()` posisi, kamera mengikuti, *Separate objects*
   dari Pohon, sudut panah ke FINISH. Lalu grup **Sampai FINISH** (menang / pesan kurang).
6. **Menemukan telur** – kondisi *Collision Petualang–Telur* dan `Status="jalan"`:
   - telur → animasi `pecah`; kepala → `kaget`; `Status="soal"`;
   - **memilih soal acak yang seimbang**: `MauYa = Random(1)`; ulangi ≤30×: ambil `SoalIdx` acak;
     jika `MauYa=1` dan `Soal[SoalIdx].bab = BabTarget` → cocok (jawaban "ya"); jika `MauYa=0` dan
     bab ≠ BabTarget → cocok (jawaban "tidak"). Jadi ±50% soalnya berjawab "Ya".
   - tentukan `Kunci` ("ya"/"tidak"), isi teks panel, tampilkan `GrupSoal`;
   - (opsional) 1 blok JavaScript memutar bacaan Arab `Soal[SoalIdx].suara`.
7. **Menjawab** – klik `TombolYa`/`TombolTidak` → `Jawaban`. Telur yang pecah dihapus (posisinya
   di layar disimpan dulu ke `TelurLayarX/Y`). Lalu:
   - `Jawaban = Kunci` → **benar** (`Status="hasil"`): `Skor + 1`, suara "Benar!", dan **efek masuk
     keranjang**: dibuat `Telur` baru di layer UI di posisi tadi, lalu *Tween* posisi ke `Keranjang`
     (0,8 dtk). Saat tween selesai → "ding", telur dihapus, keranjang membesar sebentar (tween skala).
   - `Jawaban ≠ Kunci` → **salah** (`Status="salah"`): kepala `kaget`, lalu adegan bertahap di grup
     *Adegan SALAH* (lihat tabel di atas): jadi telur + efek `Asap`, kelinci datang dengan kepala
     `marah` + suara, wazan yang benar ditampilkan di panel bawah, lalu tanya mulai lagi.
8. **Selesai menampilkan hasil BENAR** – timer `hasil` > `LamaHasil` → panel disembunyikan, buat telur
   baru, `Status="jalan"`; jika `Skor >= TargetTelur` → *Change scene* `Menang`.

Panel soal (tengah) hanya tampil saat `"soal"`. Panel hasil & pertanyaan "mulai lagi" ada di **bawah
layar** supaya petualang (yang jadi telur) dan kelinci di tengah tidak tertutup.

## 5a. Koleksi boneka & penyimpanan (Storage)
- `Koleksi` = variabel global array 6 angka = jumlah menang per wazan.
- Scene Menang (adegan bertahap dengan timer `menang` + variabel `Tahap`): 1,2 dtk kelinci POP (asap)
  berubah jadi `Boneka`; 2,6 dtk boneka *tween* terbang mengecil ke tombol RAK BONEKA; sampai → "ding",
  tombol membesar sebentar, jumlah boneka ditampilkan. `Koleksi[BabTarget-1] + 1`, lalu aksi
  *Storage → Save a text*: nama penyimpanan `"TelurWazan"`, kunci `"koleksi"`, isi `ToJSON(Koleksi)`.
- Scene Menu & Koleksi (grup *Muat koleksi*): jika *Group exists* → *Load a text* ke variabel scene
  `KoleksiJSON` → aksi *Convert JSON to a variable* ke `Koleksi`.
- Boneka: objek `Boneka` punya animasi `b<bab>_t<tingkat>` (6 warna × 4 tingkat) + `kosong`.
  Nama animasinya dihitung: `"b" + bab + "_t" + clamp(Koleksi[bab-1], 1, 4)` → menang ke-1 polos,
  ke-2 pita, ke-3 topi, ke-4 dan seterusnya mahkota (jumlahnya tetap dihitung: ×N).

## 5. Bagaimana data soal disimpan

Variabel global `Soal` adalah **array** berisi **structure**:
```
Soal[0] = { madhi: "نَصَرَ", mudhari: "يَنْصُرُ", arti: "menolong", bab: 1, suara: "audio/soal/nashara.mp3" }
Soal[1] = { ... }
```
`NamaBab` = array 6 teks: `NamaBab[0]` = "فَعَلَ - يَفْعُلُ" (bab 1) … `NamaBab[5]` (bab 6).
Karena indeks array mulai dari 0, di event dipakai `NamaBab[BabTarget - 1]`.

Menambah soal di GDevelop: *Project manager → Global variables → Soal → tambah item* lalu isi
5 anaknya. Kolom `suara` boleh dikosongkan (tidak ada bacaan) atau isi nama file mp3 baru yang
sudah ditambahkan ke *Resources*.

## 6. Ide latihan bertahap untuk anak-anak

1. **Ubah angka**: `TargetTelur` jadi 3, kecepatan petualang jadi 400. Lihat efeknya.
2. **Ubah gambar**: gambar kepala petualang versi sendiri (56×56 px, PNG transparan), timpa
   `assets/petualang_kepala_normal.png`.
3. **Tambah soal**: tambah 3 fi'il favorit ke `Soal`.
4. **Ubah kalimat**: ganti teks "Salah! Wazan yang benar:" di event *Menjawab*.
5. **Tambah event baru**: misalnya *saat benar → kelinci muncul dan tersenyum* (tinggal salin aksi
   dari cabang "salah", ganti animasinya `biasa`).
6. **Ubah peta**: di grup *Buat peta acak*, ganti jumlah titik (5 → 7) atau lebar jalur (3 → 2 sel),
   atau tambah "jalan buntu" cabang acak. Lihat efeknya langsung.
7. **Tingkat boneka baru**: gambar `boneka_bX_t5.png` (mis. sayap), tambah animasi `bX_t5`, ubah
   `clamp(..., 1, 4)` jadi `1, 5`.
8. **Tambah scene**: layar "Pilih tokoh" sebelum Menu.

## 7. Catatan teknis
- Teks Arab memakai font **Amiri** (dibundel di `assets/fonts`). Objek teks Arab diberi *padding*
  lewat aksi *Text → Padding* saat scene mulai, supaya harakat di atas huruf tidak terpotong.
- Satu-satunya blok JavaScript (di event *Menemukan telur*) hanya untuk memutar file suara yang
  namanya diambil dari variabel — aksi *Play a sound* biasa tidak bisa memilih file dari variabel.
  Blok itu aman dihapus/dinonaktifkan; game tetap jalan tanpa bacaan Arab.
- Semua objek dibuat "kecil-kecil": tanpa extension tambahan, supaya mudah dipelajari.
