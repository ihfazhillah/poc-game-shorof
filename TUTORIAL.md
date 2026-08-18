# Tutorial: Memahami "Telur Wazan" di GDevelop — Langkah demi Langkah

Panduan **hands-on** untuk memahami cara kerja game ini **di dalam GDevelop**, disusun agar
bisa kamu pelajari sebagai developer **dan** kamu ajarkan ke anak-anak. Filosofinya:
buka game → jalankan → telusuri → ubah sedikit → lihat hasilnya → ulangi.

> **Intinya ada di GDevelop.** File `game.json` cukup dibuka di GDevelop; di sanalah semua
> logika, scene, dan objek bisa dilihat dan diubah. (Skrip Python di `tools/` hanya membuat
> *titik awal* proyek ini — penjelasannya ada di [Lampiran A](#lampiran-a--skrip-python-titik-awal-opsional),
> dan **tidak perlu** untuk belajar/mengajar.)
>
> **Suara:** kita **tidak** memakai text-to-speech. Anak-anak akan **mengisi suaranya sendiri**
> (merekam). Caranya ada di [Bagian 9](#bagian-9--anak-anak-mengisi-suara-sendiri).

Dokumen pendamping: `README.md` (cara main), `PANDUAN-GDEVELOP.md` (peta isi proyek),
`RENCANA.md` (keputusan desain).

---

## Bagian 0 — Siapkan & jalankan dulu

1. Pasang **GDevelop 5** (desktop dari <https://gdevelop.io>, atau web
   <https://editor.gdevelop.io>). Dibuat/diuji dengan pustaka inti 5.6.x.
2. **File → Open** → pilih `game.json` di folder ini.
3. Tekan tombol **Preview** (▶). Mainkan: pilih wazan, jalan pakai panah/WASD, sentuh telur,
   jawab YA/TIDAK, cari 5 telur, ke FINISH.

> **Ajak anak:** mainkan dulu bareng sampai mereka paham *apa* yang terjadi, sebelum melihat
> *bagaimana* itu dibuat. Rasa penasaran "kok bisa?" adalah bahan bakar belajarnya.

Prinsip belajar sepanjang tutorial ini: **satu perubahan dalam satu waktu, lalu selalu tekan
Preview.** Kalau rusak, kamu tahu persis penyebabnya.

---

## Bagian 1 — Tiga kata ajaib GDevelop

Semua game di GDevelop dibangun dari tiga hal saja. Ini bahasa yang bisa langsung dipakai ke anak:

| Kata | Untuk anak | Contoh di game ini |
|---|---|---|
| **Scene** (adegan) | "Layar / panggung" | Menu, Hutan, Menang, Koleksi |
| **Objek** | "Pemain di panggung" (gambar/tulisan) | Petualang, Telur, Kelinci, tombol, teks skor |
| **Event** | "Aturan: **JIKA** … **MAKA** …" | JIKA sentuh telur MAKA telur pecah |

Ditambah satu lagi: **Variabel** = "kotak untuk menyimpan angka/tulisan" (mis. skor, wazan
yang dipilih).

Satu hal penting soal **Event**: aturannya diperiksa **terus-menerus, ±60 kali per detik**.
Jadi "JIKA petualang menyentuh telur" itu seperti penjaga yang mengecek tanpa henti.

> **Ajak anak:** main peran. Satu anak jadi "Event/penjaga aturan" yang terus mengulang
> "kalau kamu pegang telur, telurnya pecah ya!". Anak lain jadi "Petualang". Begitulah event bekerja.

---

## Bagian 2 — Tur proyek (Project manager)

Di kiri GDevelop ada **Project manager**. Buka dan telusuri (belum mengubah apa pun):

```
Project manager
├─ Game settings
├─ Scenes ............ Menu · Hutan · Menang · Koleksi     ← 4 panggung
├─ Objects (global) .. Petualang, KepalaPetualang, Kelinci, Telur, Keranjang, Pohon, … Boneka
└─ Variables (global)  TargetTelur, BabTarget, NamaBab, Soal, Koleksi, …
```

- **Scenes**: klik dua kali sebuah scene untuk membukanya.
- **Objects (global)**: objek yang dipakai di banyak scene (mis. Petualang muncul di Menu,
  Hutan, Menang).
- **Variables (global)**: "kotak" yang berlaku di semua scene.

> **Ajak anak:** minta mereka menyebutkan objek yang mereka *lihat* saat bermain, lalu
> temukan namanya di daftar Objects. Menghubungkan "yang di layar" dengan "namanya di editor"
> adalah langkah pemahaman pertama.

---

## Bagian 3 — Scene = panggung (mulai dari Menu)

Buka scene **Menu** (klik dua kali). Ada dua tab penting di atas: **Scene** (menata objek) dan
**Events** (aturan).

Di tab **Scene** kamu melihat **instance** — yaitu salinan objek yang benar-benar diletakkan
di panggung (judul, 6 tombol wazan, petualang, kelinci, telur hiasan).

**Latihan 3 — ubah judul:**
1. Klik teks **"Telur Wazan"** di panggung.
2. Di panel kanan (Properties), ubah tulisannya, mis. jadi nama anakmu + "Wazan".
3. **Preview.** Judul berubah.

> **Beda "Objek" vs "Instance":** Objek = cetakan/definisi. Instance = hasil cetak yang
> diletakkan di scene. Satu objek `TombolBab` dicetak **6 kali** menjadi 6 tombol.

---

## Bagian 4 — Objek & animasi (tempat anak menggambar)

Klik dua kali objek **Petualang** (di daftar Objects). Kamu lihat beberapa **animasi**:

- `diam` — 1 gambar.
- `jalan` — 4 gambar berurutan (itulah kaki yang bergerak).
- `telur` — gambar saat petualang "berubah jadi telur" ketika salah.

**Kepala terpisah dari badan.** Ada objek `Petualang` (badan) dan `KepalaPetualang` (kepala).
Itu sengaja: supaya wajah bisa ganti ekspresi (`normal` / `kaget`) tanpa mengganggu animasi
jalan. Di scene Hutan, sebuah event menempelkan kepala ke badan setiap frame.

**Latihan 4 — ganti gambar dengan karya anak (INI bagian serunya):**
1. Minta anak menggambar kepala petualang (kertas → foto/scan, atau langsung digital), ukuran
   mirip aslinya, latar transparan (PNG).
2. Timpa file `assets/petualang_kepala_normal.png` dengan gambar itu (nama sama).
3. Di GDevelop, buka animasi `normal` objek `KepalaPetualang` → pastikan menunjuk gambar itu
   (kalau nama file sama, otomatis). **Preview** — tokohnya kini buatan anak.

> **Ajak anak:** biarkan mereka menggambar telur, kelinci, atau pohon versi sendiri. Nama
> file harus sama supaya langsung terpakai. Ini membuat game terasa "milik mereka".
> Detail teknis mata berbentuk hamzah (ء) & daftar file ada di `PANDUAN-GDEVELOP.md`.

---

## Bagian 5 — Event = JIKA … MAKA … (baca aturan pertama)

Buka scene **Menu** → tab **Events**. Cari aturan klik tombol. Dibaca begini:

```
JIKA  kursor berada di atas TombolBab
 DAN  tombol kiri mouse dilepas
MAKA  BabTarget = (nomor bab tombol itu)
 DAN  mainkan bunyi klik
 DAN  pindah ke scene "Hutan"
```

Itu saja logika sebuah tombol: syarat di atas (kondisi), tindakan di bawah (aksi). Semua
game ini hanyalah tumpukan aturan seperti ini.

**Latihan 5 — ubah aksi:** temukan event **Saat mulai** di scene mana pun yang mengeset
sebuah teks, dan ubah tulisannya. Atau di scene **Hutan**, cari kalimat *"Salah! Wazan yang
benar:"* dan ganti kata-katanya. **Preview.**

> **Ajak anak:** tekankan urutan **JIKA → MAKA**. Tanya: "aturan apa yang kamu mau?" mis.
> "JIKA menang MAKA muncul tulisan HORE". Nanti kalian buat bersama di Bagian 12.

---

## Bagian 6 — Variabel (kotak penyimpan)

Buka **Project manager → Variables (global)**. Beberapa yang penting:

| Variabel | Isi | Coba ubah |
|---|---|---|
| `TargetTelur` | berapa telur harus dikumpulkan (5) | jadikan **3** → Preview, lebih cepat menang |
| `JumlahTelurDiHutan` | berapa telur disebar (10) | harus **≥** `TargetTelur` |
| `BabTarget` | wazan yang sedang dilatih (diisi saat klik menu) | — |
| `NamaBab` | daftar 6 nama wazan (teks Arab) | ganti/tambah tulisan wazan |
| `Soal` | daftar 81 fi'il (`madhi`, `mudhari`, `arti`, `bab`, `suara`) | tambah fi'il favorit |

**Latihan 6a — lebih mudah:** `TargetTelur` = 3. Preview.

**Latihan 6b — tambah soal:** buka `Soal` → tambah item baru → isi 5 anaknya (`madhi`,
`mudhari`, `arti`, `bab`, dan `suara` boleh dikosongkan). Preview, cari telur, lihat fi'il
barumu muncul.

Ada juga variabel **scene** (khusus satu scene). Yang paling penting: `Status` di scene Hutan
— dibahas berikut.

> **Ajak anak:** variabel = "papan skor" atau "kotak ingatan". Ubah `TargetTelur` bareng dan
> minta mereka menebak apa yang akan terjadi sebelum menekan Preview.

---

## Bagian 7 — "Mode" permainan: variabel `Status` (scene Hutan)

Buka scene **Hutan**. Seluruh permainan diatur oleh satu variabel scene bernama `Status`
— anggap saja **"mode" yang sedang aktif**. Hampir setiap aturan diawali "JIKA Status = …"
supaya aturan tidak saling bertabrakan.

| `Status` | Artinya | Pindah ke mode berikut ketika |
|---|---|---|
| `jalan` | bebas berjalan mencari telur | menyentuh telur |
| `soal` | telur pecah, panel soal muncul, gerak dikunci | klik YA / TIDAK |
| `hasil` | jawaban **benar**, telur terbang ke keranjang | beberapa detik berlalu |
| `salah` | adegan: berubah jadi telur → kelinci datang marah | selesai adegan |
| `tanya_ulang` | "Mau mulai lagi?" | YA → ulang · TIDAK → Menu |

> **Ajak anak:** analogi lampu lalu lintas. "Mode `jalan` = hijau (boleh gerak). Mode `soal`
> = merah (berhenti, jawab dulu)." Ini konsep **state machine** — sangat berguna untuk game
> apa pun, dan mudah dipahami anak lewat analogi "mode".

Coba telusuri di tab **Events** scene Hutan: perhatikan betapa banyak event dimulai dengan
kondisi `Status = "..."`. Itulah rahasia rapinya logika game.

---

## Bagian 8 — Peta yang berbeda setiap main (procedural)

Perhatikan: setiap kali mulai, **jalur hutannya berbeda**. Di tab **Scene** Hutan malah
hampir kosong (tidak ada pohon!). Rahasianya: peta **dibuat oleh event saat scene mulai**,
bukan diletakkan tangan.

Buka tab **Events** Hutan → grup **"Buat peta acak"**. Ringkasnya (baca komentar di tiap
langkah — sudah ditulis dalam bahasa Indonesia di dalam event):

1. Hutan dibagi jadi **grid 20 × 14 kotak**.
2. Pilih beberapa **titik jalur** dari kiri (START) ke kanan (FINISH), tingginya **diacak**.
3. Titik disambung jadi jalur; kotak lain **ditanami pohon** (pohon = penghalang).
4. **Telur** disebar di kotak jalur yang acak.

**Latihan 8 — ubah satu angka:** di grup itu, cari lebar jalur (3 kotak) atau jumlah titik,
ubah **satu** angka, lalu **Preview** beberapa kali dan lihat petanya berubah. Kalau aneh,
kembalikan angkanya.

> **Ajak anak:** ini "membuat labirin otomatis". Mereka tak perlu paham semua matematikanya;
> cukup rasakan bahwa **aturan sederhana → dunia yang selalu baru**. Itu ide besar
> (*procedural generation*) yang membekas.

---

## Bagian 9 — Anak-anak mengisi suara sendiri

Game ini memutar file suara dari folder `audio/`. **Tidak ada** yang mengunci suaranya harus
buatan mesin — silakan **rekam suara anak** dan pakai itu. Dua jenis suara:

- `audio/suara/` — kalimat narator & kelinci (mis. `benar.mp3`, `salah.mp3`, `menang.mp3`,
  `mulai.mp3`, `mulai_lagi.mp3`, `kurang.mp3`, `boneka.mp3`).
- `audio/soal/` — bacaan tiap fi'il (mis. `nashara.mp3`) dan nama wazan (`wazan1.mp3`…).

**Cara mengganti dengan rekaman anak (paling mudah — nama file sama):**
1. Rekam suara (HP/laptop), simpan sebagai **mp3** (atau wav/ogg).
2. Beri nama **persis sama** dengan file yang ingin diganti, mis. `benar.mp3`.
3. Timpa file lama di folder `audio/…`. Selesai — game langsung memakai suara baru saat Preview.

**Menambah suara baru (nama file baru):**
1. Simpan rekaman ke `audio/suara/` (mis. `hore.mp3`).
2. Di GDevelop: **Project manager → Resources → Add** → pilih file itu (mendaftarkannya).
3. Di sebuah event, tambahkan aksi **Audio → Play a sound**, pilih `hore.mp3`.

> **Ajak anak:** bagi tugas — satu anak jadi "narator" (Ayo cari telur!), satu jadi "kelinci"
> yang lucu, satu membaca fi'il Arab. Merekam suara sendiri membuat mereka merasa **memiliki**
> game-nya. Untuk memilih *kapan* suara berbunyi, lihat event yang memakai **Play a sound**
> (mis. saat benar/salah/menang).
>
> Catatan: ada satu file suara `mp3` per fi'il karena nama filenya diambil dari kolom `suara`
> di variabel `Soal`. Kalau kamu tak mau ada bacaan untuk suatu fi'il, kosongkan saja kolom
> `suara`-nya.

---

## Bagian 10 — Koleksi boneka & menyimpan kemajuan

Setiap kali menang, kelinci berubah jadi **boneka koleksi** yang tersimpan **di perangkat**
(tidak hilang saat game ditutup), dan bonekanya **naik tingkat** tiap menang lagi:
polos → pita → topi → mahkota.

- Jumlah kemenangan tiap wazan disimpan di variabel `Koleksi` (6 angka).
- Scene **Menang** menambah `Koleksi` lalu **menyimpannya** (aksi *Storage*).
- Scene **Menu** & **Koleksi** **memuatnya** kembali saat dibuka.
- Tombol **Rak Boneka** di Menu membuka scene **Koleksi**.

Ini contoh sederhana **menyimpan data antar-sesi**. Tak perlu diubah untuk belajar; cukup
tahu di mana letaknya (grup event *Muat koleksi* & aksi simpan di scene Menang).

> **Ajak anak:** "Rak boneka" adalah hadiah yang membuat mereka ingin menang lagi. Diskusikan:
> hadiah apa lagi yang seru? (Itu bisa jadi ide fitur berikutnya.)

---

## Bagian 11 — Preview, lalu bagikan (export web)

- **Preview (▶)** = cara utama menguji tiap perubahan. Pakai sesering mungkin.
- **Export → Web (HTML5)** menghasilkan game siap dibuka di browser (masuk ke `build-web/`).
- Menjalankan versi web (jangan buka `index.html` lewat klik dua kali — browser memblokir
  font/suara dari `file://`):

```bash
bash tools/jalankan_web.sh          # buka http://localhost:8090
# atau: cd build-web && python3 -m http.server 8090
```

> Kalau tampilan web terlihat "lama" (harakat terpotong), itu cache browser — tekan
> **Ctrl+Shift+R**.

---

## Bagian 12 — Cara mengajar anak (urutan bertahap)

Susun sesi dari yang paling terlihat hasilnya ke yang paling menantang. **Selalu: satu
perubahan → Preview.**

1. **Main dulu** sampai paham alurnya.
2. **Ubah angka** — `TargetTelur` = 3, atau kecepatan petualang. Efek langsung terasa.
3. **Ganti gambar** — anak menggambar kepala/telur/pohon sendiri (Bagian 4).
4. **Isi suara** — anak merekam suara narator/kelinci/bacaan (Bagian 9).
5. **Ubah kalimat** — ganti teks "Salah! Wazan yang benar:" (Bagian 5).
6. **Tambah soal** — 3 fi'il favorit (Bagian 6b).
7. **Buat event baru bersama** — mis. *JIKA benar MAKA kelinci muncul dan tersenyum*
   (salin aksi dari cabang "salah", ganti animasi kelinci jadi `biasa`).
8. **Ubah peta** — satu angka di grup *Buat peta acak* (Bagian 8).
9. **Tingkat boneka baru / scene baru** — untuk yang sudah pede (lihat `PANDUAN-GDEVELOP.md` §6).

Tips mengajar:
- **Bahasa "JIKA–MAKA"** dipakai terus; itu inti berpikir logis (dan pemrograman).
- **Rayakan kesalahan.** Kalau Preview rusak, itu kesempatan belajar: "aturan tadi bilang apa?"
- **Kaitkan ke shorof.** Saat menjawab telur, tanyakan *kenapa* fi'il itu masuk/ tidak masuk
  wazan — game jadi alat, bukan tujuan.

---

## Bagian 13 — Di balik layar GDevelop (untuk kamu, developer)

Sekadar konteks agar tak "ajaib":

- **Event bukan ditafsir satu-satu saat main.** Saat Preview/Export, GDevelop meng-*compile*
  seluruh event tiap scene menjadi **fungsi JavaScript** (engine-nya bernama **GDJS**), lalu
  fungsi itu dipanggil **tiap frame**. Itu sebabnya event terasa "jalan terus", dan mengapa
  guard `JIKA Status = "..."` penting (kalau tidak, blok salah ikut jalan 60×/detik).
- **`game.json` adalah data.** Ia serialisasi objek proyek GDevelop (scenes/objects/events/
  variables/resources). Editor hanyalah UI di atasnya; kamu bisa membuka file itu dengan
  editor teks dan melihat strukturnya.
- **Behavior itu "gratis".** *Top-down movement* (jalan pakai panah) dan *Tween* (animasi
  gerak halus) adalah perilaku siap pakai; kita cukup memasangnya ke objek, tanpa menulis
  logika gerak sendiri.
- **Resources = jembatan file.** Runtime hanya memuat gambar/suara yang terdaftar di daftar
  *Resources*. Maka saat menambah file baru, daftarkan lewat **Resources → Add**.

Sumber resmi: [GDevelop — Events](https://wiki.gdevelop.io/gdevelop5/events/),
[Events editor](https://wiki.gdevelop.io/gdevelop5/interface/events-editor/),
[GDJS Runtime — RuntimeScene](https://docs.gdevelop.io/GDJS%20Runtime%20Documentation/classes/gdjs.RuntimeScene.html),
[Project Manager](https://wiki.gdevelop.io/gdevelop5/interface/project-manager/).

---

## Lampiran A — Skrip Python (titik awal, opsional)

Proyek ini **awalnya** dibuat otomatis oleh skrip di `tools/` supaya langsung ada untuk
dipelajari. **Untuk belajar & mengajar, kamu tidak perlu menjalankannya** — cukup kerja di
GDevelop.

| Skrip | Membuat | Catatan |
|---|---|---|
| `tools/soal.py` | daftar 81 fi'il + 6 nama wazan | sumber data (dipakai skrip lain) |
| `tools/buat_aset.py` | gambar `assets/*.png` (pakai Pillow) | bisa dijalankan ulang untuk regen gambar |
| `tools/buat_audio.py` | suara di `audio/` | **tidak dipakai lagi** untuk suara utama — anak merekam sendiri (Bagian 9) |
| `tools/buat_game.py` | `game.json` itu sendiri | lihat peringatan di bawah |

⚠️ **PERINGATAN PENTING:** setelah kamu mengubah proyek **di GDevelop**, **JANGAN** jalankan
`python3 tools/buat_game.py` lagi — perintah itu **menimpa `game.json` dari nol** dan
perubahanmu di editor akan hilang. Sejak kamu mulai mengedit di GDevelop, **GDevelop adalah
satu-satunya sumber kebenaran.**

(Kalau suatu saat kamu ingin membuat ulang **gambar** dari kode, `buat_aset.py` masih aman
dijalankan karena hanya menulis ke `assets/`. Detail cara kerja generator ada di komentar
tiap file.)
