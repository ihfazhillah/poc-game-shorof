#!/usr/bin/env python3
"""
Membuat semua suara untuk game "Telur Wazan".

Jalankan:  python3 tools/buat_audio.py            (semua)
           python3 tools/buat_audio.py --tanpa-tts (hanya efek suara & musik, tanpa internet)

Hasil:
  audio/suara/*.mp3   -> kalimat suara (TTS): benar, salah (kelinci), menang, mulai
  audio/soal/*.mp3    -> bacaan Arab tiap contoh fi'il (TTS bahasa Arab)
  audio/sfx/*.wav     -> efek suara sintetis (pecah, ding, buzz, klik)

TTS memakai `edge-tts` (sudah terpasang di PC ini; butuh internet). MeloTTS tidak
mendukung bahasa Indonesia/Arab, jadi tidak dipakai. Kalau ingin ganti backend TTS,
cukup ubah fungsi `tts()` di bawah.
"""
import sys, subprocess, math, wave, struct, shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from soal import daftar_soal, NAMA_BAB  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "audio"
for sub in ("suara", "soal", "sfx"):
    (AUDIO / sub).mkdir(parents=True, exist_ok=True)

SUARA_ID = "id-ID-GadisNeural"     # narator (perempuan)
SUARA_KELINCI = "id-ID-ArdiNeural"  # kelinci (nanti nadanya dinaikkan)
SUARA_AR = "ar-SA-HamedNeural"      # bacaan Arab

TANPA_TTS = "--tanpa-tts" in sys.argv


# --------------------------------------------------------------------------
# TTS
# --------------------------------------------------------------------------
def tts(teks: str, tujuan: Path, voice: str, rate: str = "+0%", pitch: str = "+0Hz"):
    """Buat file mp3 dari teks. Ganti isi fungsi ini kalau ingin pakai TTS lain."""
    if tujuan.exists():
        print("  (ada) ", tujuan.relative_to(ROOT))
        return
    cmd = ["edge-tts", "--voice", voice, "--rate", rate, "--pitch", pitch,
           "--text", teks, "--write-media", str(tujuan)]
    subprocess.run(cmd, check=True, capture_output=True)
    print("  tts   ", tujuan.relative_to(ROOT))


def suara_kelinci(teks: str, tujuan: Path):
    """Suara kelinci: TTS lalu nada dinaikkan dengan ffmpeg supaya lucu."""
    if tujuan.exists():
        print("  (ada) ", tujuan.relative_to(ROOT))
        return
    sementara = tujuan.with_suffix(".tmp.mp3")
    tts(teks, sementara, SUARA_KELINCI, rate="+10%")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(sementara),
                    "-af", "asetrate=24000*1.35,aresample=24000,atempo=0.85",
                    str(tujuan)], check=True)
    sementara.unlink()
    print("  kelinci", tujuan.relative_to(ROOT))


# --------------------------------------------------------------------------
# Efek suara sintetis (tanpa library tambahan: hanya math + wave)
# --------------------------------------------------------------------------
SR = 22050


def simpan_wav(nama: Path, sampel):
    with wave.open(str(nama), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, s)) * 32000)) for s in sampel))
    print("  sfx   ", nama.relative_to(ROOT))


def nada(freq, durasi, vol=0.5, bentuk="sine", decay=6.0):
    n = int(SR * durasi)
    out = []
    for i in range(n):
        t = i / SR
        env = math.exp(-decay * t)
        if bentuk == "sine":
            v = math.sin(2 * math.pi * freq * t)
        elif bentuk == "square":
            v = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
        else:  # segitiga
            v = 2 * abs(2 * ((t * freq) % 1) - 1) - 1
        out.append(v * env * vol)
    return out


def gabung(*bagian):
    out = []
    for b in bagian:
        out.extend(b)
    return out


def campur(a, b, offset=0):
    n = max(len(a), offset + len(b))
    out = [0.0] * n
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[offset + i] += v
    return out


def sfx_pecah():
    import random
    random.seed(3)
    n = int(SR * 0.35)
    out = []
    for i in range(n):
        t = i / SR
        env = math.exp(-14 * t)
        v = random.uniform(-1, 1) * env
        # dua "krek" berurutan
        if 0.10 < t < 0.13 or 0.20 < t < 0.24:
            v *= 2.5
        out.append(v * 0.6)
    return out


def sfx_ding():
    return campur(nada(880, 0.35, 0.4), nada(1320, 0.5, 0.35), int(SR * 0.12))


def sfx_buzz():
    return gabung(nada(150, 0.18, 0.5, "square", 4), [0.0] * int(SR * 0.05),
                  nada(120, 0.30, 0.5, "square", 4))


def sfx_pop():
    """Suara 'pop' saat berubah jadi telur: nada meluncur turun."""
    n = int(SR * 0.25)
    out = []
    fase = 0.0
    for i in range(n):
        t = i / SR
        f = 900 - 2200 * t
        fase += 2 * math.pi * max(f, 80) / SR
        out.append(math.sin(fase) * math.exp(-9 * t) * 0.6)
    return out


def sfx_klik():
    return nada(1000, 0.06, 0.4, "sine", 40)


def sfx_menang():
    do, mi, sol, do2 = 523, 659, 784, 1046
    return gabung(nada(do, 0.18, 0.4, "segitiga", 5), nada(mi, 0.18, 0.4, "segitiga", 5),
                  nada(sol, 0.18, 0.4, "segitiga", 5), nada(do2, 0.6, 0.45, "segitiga", 3))


def musik_latar(nama: Path):
    """Musik latar 8 birama sederhana (pentatonik), diulang (loop) di game."""
    if nama.exists():
        print("  (ada) ", nama.relative_to(ROOT))
        return
    bpm = 100
    ketuk = 60 / bpm
    # C pentatonik: C D E G A
    melodi = [523, 587, 659, 784, 659, 587, 523, 440,
              523, 659, 784, 880, 784, 659, 587, 523,
              440, 523, 587, 659, 587, 523, 440, 392,
              523, 587, 659, 784, 880, 784, 659, 523]
    bass = [262, 262, 220, 220, 196, 196, 262, 262]
    total = int(SR * ketuk * len(melodi))
    out = [0.0] * total
    for i, f in enumerate(melodi):
        n = nada(f, ketuk * 0.95, 0.18, "segitiga", 2.5)
        pos = int(i * ketuk * SR)
        for j, v in enumerate(n):
            if pos + j < total:
                out[pos + j] += v
    for i, f in enumerate(bass):
        n = nada(f, ketuk * 4 * 0.9, 0.12, "sine", 0.8)
        pos = int(i * ketuk * 4 * SR)
        for j, v in enumerate(n):
            if pos + j < total:
                out[pos + j] += v
    wav = nama.with_suffix(".wav")
    simpan_wav(wav, out)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-c:a", "libvorbis", "-q:a", "3", str(nama)], check=True)
    wav.unlink()
    print("  musik ", nama.relative_to(ROOT))


# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("== Efek suara ==")
    simpan_wav(AUDIO / "sfx" / "pecah.wav", sfx_pecah())
    simpan_wav(AUDIO / "sfx" / "ding.wav", sfx_ding())
    simpan_wav(AUDIO / "sfx" / "buzz.wav", sfx_buzz())
    simpan_wav(AUDIO / "sfx" / "klik.wav", sfx_klik())
    simpan_wav(AUDIO / "sfx" / "pop.wav", sfx_pop())
    simpan_wav(AUDIO / "sfx" / "menang.wav", sfx_menang())
    # Musik latar sengaja TIDAK dibuat/dipakai (permintaan): fungsi musik_latar() dibiarkan
    # sebagai contoh saja.

    if TANPA_TTS:
        print("Lewati TTS (--tanpa-tts).")
        sys.exit(0)

    if not shutil.which("edge-tts"):
        print("edge-tts tidak ditemukan. Pasang: pip install edge-tts   (atau jalankan dengan --tanpa-tts)")
        sys.exit(1)

    print("== Suara narator ==")
    tts("Ayo cari telur di hutan!", AUDIO / "suara" / "mulai.mp3", SUARA_ID)
    tts("Benar! Telur masuk keranjang.", AUDIO / "suara" / "benar.mp3", SUARA_ID)
    tts("Hebat! Semua telur sudah terkumpul!", AUDIO / "suara" / "menang.mp3", SUARA_ID)
    tts("Pilih wazan yang ingin kamu latih.", AUDIO / "suara" / "pilih_wazan.mp3", SUARA_ID)
    print("== Suara kelinci (marah) ==")
    suara_kelinci("Salah! Kamu berubah jadi telur! Ayo belajar lagi!", AUDIO / "suara" / "salah.mp3")
    suara_kelinci("Aduh, salah lagi! Perhatikan harakatnya!", AUDIO / "suara" / "salah2.mp3")
    tts("Mau mulai lagi dari awal?", AUDIO / "suara" / "mulai_lagi.mp3", SUARA_ID)
    tts("Hore! Kelinci jadi bonekamu!", AUDIO / "suara" / "boneka.mp3", SUARA_ID)
    tts("Telurnya masih kurang. Ayo cari lagi!", AUDIO / "suara" / "kurang.mp3", SUARA_ID)

    print("== Bacaan Arab: nama wazan ==")
    for i, nama in enumerate(NAMA_BAB, start=1):
        tts(nama.replace(" - ", " "), AUDIO / "soal" / f"wazan{i}.mp3", SUARA_AR, rate="-10%")
    print("== Bacaan Arab: tiap contoh fi'il ==")
    for s in daftar_soal():
        tts(f"{s['madhi']} {s['mudhari']}", AUDIO / "soal" / f"{s['slug']}.mp3", SUARA_AR, rate="-10%")
    print("Selesai.")
