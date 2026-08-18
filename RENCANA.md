# Rencana: Telur Wazan (GDevelop)

Game edukasi shorof sederhana. Ide: anak. Implementasi awal: dibuat otomatis (aset, suara, dan proyek GDevelop) supaya tinggal dibuka di GDevelop dan langsung dicoba, lalu dipelajari & diubah bersama anak-anak.

## 1. Konsep permainan

| Hal | Keputusan v1 |
|---|---|
| Judul | Telur Wazan |
| Genre | Petualangan top-down (dilihat dari atas) di hutan, cari telur |
| Kontrol | Panah / WASD untuk jalan; klik/tap tombol **Ya** / **Tidak** |
| Target | Kumpulkan **5 telur** (variabel global `TargetTelur`, mudah diubah) |
| Wazan | Dipilih di menu awal: 6 bab tsulatsi mujarrad (فَعَلَ يَفْعُلُ, فَعَلَ يَفْعِلُ, فَعَلَ يَفْعَلُ, فَعِلَ يَفْعَلُ, فَعُلَ يَفْعُلُ, فَعِلَ يَفْعِلُ) |
| Soal | Telur disentuh → pecah → muncul contoh **fi'il madhi – mudhori'** + arti. Pertanyaan: "Apakah termasuk wazan X?" |
| Benar | Telur masuk keranjang, skor +1, suara "Benar!" |
| Salah | Petualang berubah jadi telur, kelinci muncul dan memarahi (suara), lalu kembali normal |
| Acak | Soal diacak dari daftar (variabel global `Soal`), diseimbangkan ±50% jawaban "Ya" |
| Halang rintang | Belum ada (sesuai permintaan) |
| Menang | Skor = target → layar "Hebat!" → kembali ke menu |

## 2. Struktur proyek GDevelop

```
game.json          ← proyek GDevelop (buka file ini di GDevelop)
assets/            ← gambar PNG (dibuat oleh tools/buat_aset.py)
audio/             ← suara (dibuat oleh tools/buat_audio.py)
tools/             ← skrip pembuat aset/suara/proyek (tidak dibutuhkan saat main)
README.md          ← cara buka, main, dan mengubah
PANDUAN-GDEVELOP.md← penjelasan isi proyek untuk belajar/mengajar
```

### Scene (layar)
1. **Menu** – judul + 6 tombol pilihan wazan. Klik → simpan `BabTarget` → ke scene Hutan.
2. **Hutan** – dunia rumput 2000×1400, kamera mengikuti petualang, telur muncul acak, panel soal di layer `UI`.
3. **Menang** – ucapan selamat + tombol "Main Lagi".

### Objek utama (Hutan)
- `Petualang` (badan; behavior *Top-down movement*; animasi `diam`, `jalan`, `telur`)
- `KepalaPetualang` (kepala terpisah, mengikuti badan lewat event; animasi `normal`, `kaget`)
- `Kelinci` (badan) + `KepalaKelinci` (animasi `biasa`, `marah`)
- `Telur` (animasi `utuh`, `pecah`)
- Dekorasi: `Rumput` (tiled), `Pohon`, `Semak`, `Bunga`
- UI: `Keranjang`, `TeksSkor`, `TeksWazan`, `PanelSoal`, `TeksSoalArab`, `TeksArti`, `TeksPertanyaan`, `TombolYa`, `TombolTidak`, `TeksHasil`, `TeksHasilArab`

### Variabel penting
- Global: `TargetTelur` (5), `BabTarget` (1–6), `NamaBab` (array 6 teks Arab), `Soal` (array: `madhi`, `mudhari`, `arti`, `bab`, `suara`)
- Scene Hutan: `Status` ("jalan" / "soal" / "hasil"), `Skor`, `SoalIdx`, `Jawaban`, dll.

## 3. Aset (dibuat sendiri, gaya kartun sederhana)
Kepala & badan **terpisah** untuk petualang dan kelinci. Semua PNG dibuat dengan Python/PIL sehingga bisa dibuat ulang / diubah warnanya lewat `tools/buat_aset.py`, atau diganti dengan gambar buatan anak-anak (nama file sama).

## 4. Suara
- MeloTTS tidak ditemukan di PC ini dan memang tidak mendukung bahasa Indonesia/Arab → dipakai **edge-tts** (sudah terpasang; butuh internet saat membuat) untuk: "Benar!", "Salah!" (suara kelinci dinaikkan nadanya), "Hebat!", ajakan mulai, dan bacaan tiap contoh fi'il (bahasa Arab).
- Efek (pecah, ding, buzz, pop) dibuat sintetis. Tanpa musik latar sama sekali (permintaan).
- Skrip: `tools/buat_audio.py` (fungsi TTS mudah diganti backend lain).

## 5. Verifikasi
Proyek divalidasi memakai pustaka inti GDevelop (libGD.js, versi 5.6.x): semua kondisi/aksi dicek, di-*export* ke HTML5, lalu dimainkan di browser untuk memastikan alur berjalan.

## 6. Perubahan setelah dicoba anak-anak (16 Agustus 2026)
- Peta START → FINISH yang **diacak tiap main** (grid 20×14, jalur huruf-L, pohon = penghalang).
- Menang hanya saat sampai FINISH dengan telur cukup; kurang → boleh balik.
- Hadiah: **kelinci jadi boneka koleksi** (rak 6 wazan, ×N, naik tingkat; tersimpan di perangkat).
- Salah: adegan bertahap (jadi telur → dimarahi → tanya mulai lagi), panel di bawah agar tidak menutupi.
- Efek telur terbang ke keranjang; mata semua tokoh = huruf hamzah; tanpa musik sama sekali.

## 7. Status (16 Agustus 2026)
Selesai & teruji: `game.json` (3 scene, 11 objek global, 81 soal), 28 gambar, 96 file suara,
export HTML5 di `build-web/`. Alur Menu → Hutan → 5 telur (benar & salah) → Menang → Menu
sudah dijalankan otomatis di browser (headless Chrome) tanpa error.

Belum dibuat (sengaja, sesuai permintaan): halang rintang, musuh, level. Ide lanjutan ada di
PANDUAN-GDEVELOP.md bagian 6.
