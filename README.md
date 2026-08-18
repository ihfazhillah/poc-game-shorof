# Telur Wazan 🥚

Game edukasi shorof sederhana dibuat dengan **GDevelop 5**. Ide: anak-anak.

> Petualang berjalan dari **START** ke **FINISH** lewat jalur hutan yang **diacak setiap kali main**,
> sambil mencari telur. Telur yang disentuh akan pecah dan memperlihatkan contoh fi'il madhi – mudhori'.
> Petualang harus menjawab: *apakah fi'il ini termasuk wazan yang dicari?* (**Ya / Tidak**).
> Benar → telur terbang masuk keranjang. Salah → petualang berubah jadi telur (POP!), kelinci datang
> memarahi, lalu ditanya "Mau mulai lagi dari awal?". Sampai FINISH dengan telur cukup → **kelinci jadi
> boneka koleksi** (rak boneka tersimpan di perangkat; boneka naik tingkat tiap kali menang lagi).

## Isi folder

| Isi | Keterangan |
|---|---|
| `game.json` | **Proyek GDevelop** — buka file ini di GDevelop |
| `assets/` | Gambar (PNG) + font (Amiri untuk Arab, Comfortaa untuk Latin) |
| `audio/` | Suara: `suara/` (narator & kelinci), `soal/` (bacaan Arab tiap fi'il), `sfx/` (efek). Tanpa musik latar. |
| `build-web/` | Versi HTML5 siap main (hasil export), untuk mencoba tanpa GDevelop |
| `tools/` | Skrip Python pembuat aset/suara/proyek (tidak diperlukan untuk bermain) |
| `RENCANA.md` | Rencana & keputusan desain |
| `PANDUAN-GDEVELOP.md` | Penjelasan isi proyek untuk belajar & mengajarkan ke anak-anak |

## Cara mencoba

### A. Langsung main (tanpa GDevelop)
```bash
cd build-web
python3 -m http.server 8090
```
lalu buka <http://localhost:8090> di browser. (Harus lewat server lokal, jangan klik dua kali `index.html`,
karena browser memblokir pemuatan font/suara dari `file://`.)

### B. Buka di GDevelop (untuk belajar & mengubah)
1. Pasang GDevelop 5 (versi 5.5 ke atas; dibuat/diuji dengan pustaka inti 5.6.x): <https://gdevelop.io> —
   ada versi desktop (AppImage/deb) dan versi web (<https://editor.gdevelop.io>, lalu *Open project* → pilih file).
2. **File → Open** → pilih `game.json` di folder ini.
3. Tekan tombol **Preview** (▶) untuk menjalankan.
4. Untuk mengekspor ulang versi web: **Export → Web (HTML5)**.

## Cara main
- **Panah** atau **W A S D**: berjalan.
- Sentuh telur → muncul soal → klik **YA** atau **TIDAK**.
- Kumpulkan **5 telur** (bisa diubah), lalu berjalan ke papan **FINISH** (panah kuning di kiri atas
  menunjukkan arahnya; **peta mini** di kanan atas menampilkan jalur, telur, START/FINISH, dan posisimu). Pohon menghalangi jalan; jalur berbeda tiap kali main. Sampai FINISH tapi
  telur kurang → boleh balik mencari lagi. Satu kali salah = permainan diulang dari awal (YA) atau
  kembali ke menu (TIDAK).
- **Rak Boneka** (tombol di Menu): tiap wazan yang berhasil diselesaikan memberi 1 boneka kelinci
  warna wazan itu; menang lagi → jumlah bertambah (×N) dan bonekanya naik tingkat: polos → pita →
  topi → mahkota. Tersimpan di perangkat (localStorage), jadi tidak hilang saat game ditutup.
- Mata semua tokoh berbentuk huruf **hamzah (ء)** — ide anak-anak.

> **Kalau tampilan terlihat "lama"** (harakat terpotong, tulisan bertumpuk): browser masih memakai
> berkas lama dari cache. Tekan **Ctrl+Shift+R** (muat ulang paksa) di halaman game.

## Yang paling sering ingin diubah
| Ingin mengubah… | Di GDevelop |
|---|---|
| Berapa telur harus dikumpulkan | *Project manager → Global variables →* `TargetTelur` |
| Berapa telur ditaruh di jalur | Global variables → `JumlahTelurDiHutan` (harus ≥ `TargetTelur`) |
| Bentuk/ukuran peta acak | Scene Hutan → grup event *Buat peta acak* (jumlah titik jalur, rentang acaknya, lebar jalur) |
| Menghapus koleksi boneka | Hapus penyimpanan "TelurWazan" (di browser: localStorage), atau tambah tombol reset di scene Koleksi |
| Daftar soal (fi'il, arti, bab) | Global variables → `Soal` (array; tiap item punya `madhi`, `mudhari`, `arti`, `bab`, `suara`) |
| Nama-nama wazan | Global variables → `NamaBab` |
| Kecepatan jalan | Objek `Petualang` → behavior *Top-down movement* → *Max speed* |
| Gambar | Ganti file di `assets/` dengan nama yang sama, atau ganti di editor objek |
| Kalimat suara | Edit `tools/buat_audio.py`, jalankan lagi (`python3 tools/buat_audio.py`) |

Penjelasan lebih lengkap: **PANDUAN-GDEVELOP.md**.

## Membuat ulang aset / suara / proyek (opsional)
Semua aset dibuat oleh skrip Python (butuh `pillow`; suara butuh `edge-tts` + internet dan `ffmpeg`):
```bash
python3 tools/buat_aset.py    # gambar -> assets/
python3 tools/buat_audio.py   # suara  -> audio/   (tambahkan --tanpa-tts kalau tanpa internet)
python3 tools/buat_game.py    # game.json  <-- HATI-HATI: menimpa perubahan yang dibuat di GDevelop
```
`tools/soal.py` berisi daftar soal awal (dipakai `buat_game.py` dan `buat_audio.py`).

## Catatan suara
MeloTTS tidak ditemukan di PC ini dan memang tidak mendukung bahasa Indonesia/Arab, jadi suara
dibuat dengan `edge-tts` (sudah terpasang). Suara kelinci = suara TTS yang dinaikkan nadanya
dengan ffmpeg. Efek suara dibuat sintetis (`tools/buat_audio.py`).

## Lisensi aset
Gambar & suara: dibuat khusus untuk proyek ini (bebas dipakai/diubah). Font Amiri: SIL OFL
(`assets/fonts/OFL-Amiri.txt`). Font Comfortaa: SIL OFL.
