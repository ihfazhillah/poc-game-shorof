#!/usr/bin/env python3
"""
Membuat semua gambar (PNG) untuk game "Telur Wazan" dengan Python + Pillow.

Jalankan:  python3 tools/buat_aset.py
Hasil:     assets/*.png

Gaya: kartun sederhana (bentuk dasar + garis tepi gelap). Setiap gambar digambar
4x lebih besar lalu diperkecil supaya tepinya halus (anti-alias).

Kepala dan badan dibuat TERPISAH (petualang & kelinci), sesuai permintaan.
Ubah warna/ukuran di sini, jalankan lagi, lalu di GDevelop gambar otomatis ikut berubah
(nama file tetap sama).
"""
from pathlib import Path
import math, random
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
S = 4  # faktor supersampling

# ---------- warna ----------
OUTLINE = (60, 40, 30, 255)
KULIT = (247, 210, 170, 255)
KULIT_GELAP = (222, 176, 132, 255)
RAMBUT = (110, 70, 40, 255)
TOPI = (206, 170, 110, 255)
TOPI_GELAP = (170, 135, 80, 255)
BAJU = (232, 200, 130, 255)
BAJU_GELAP = (200, 165, 95, 255)
CELANA = (120, 85, 55, 255)
SEPATU = (70, 50, 40, 255)
PUTIH = (255, 255, 255, 255)
HITAM = (40, 40, 40, 255)
MERAH_PIPI = (255, 150, 150, 200)
KELINCI = (245, 245, 250, 255)
KELINCI_GELAP = (215, 215, 228, 255)
PINK = (255, 170, 190, 255)
TELUR = (255, 246, 220, 255)
TELUR_GELAP = (232, 214, 170, 255)
TELUR_BINTIK = (222, 190, 140, 255)
KERANJANG = (190, 130, 70, 255)
KERANJANG_GELAP = (140, 90, 45, 255)
RUMPUT = (118, 184, 82, 255)
RUMPUT_TERANG = (140, 205, 95, 255)
RUMPUT_GELAP = (96, 160, 66, 255)
DAUN = (70, 150, 70, 255)
DAUN_TERANG = (100, 185, 90, 255)
DAUN_GELAP = (50, 120, 55, 255)
BATANG = (130, 85, 50, 255)


def font_arab(size):
    """Font Arab (Amiri) untuk mata berbentuk huruf hamzah."""
    for k in [ROOT / "assets/fonts/Amiri-Bold.ttf", ROOT / "assets/fonts/Amiri-Regular.ttf"]:
        if k.exists():
            return ImageFont.truetype(str(k), size)
    return font(size)


def font(size, bold=True):
    """Font untuk teks yang 'dibakar' ke gambar (tombol)."""
    kandidat = [
        ROOT / "assets/fonts/Comfortaa-Bold.otf",
        Path("/usr/share/fonts/aajohan-comfortaa-fonts/Comfortaa-Bold.otf"),
        Path("/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf"),
    ]
    for k in kandidat:
        if k.exists():
            return ImageFont.truetype(str(k), size)
    return ImageFont.load_default()


class Kanvas:
    """Kanvas dengan supersampling. Semua koordinat memakai ukuran akhir (bukan x4).
    Warna dengan alpha < 255 digambar secara "composite" (tembus pandang yang benar),
    bukan menimpa pixel di bawahnya."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def _b(self, box):
        return [box[0] * S, box[1] * S, box[2] * S, box[3] * S]

    def _gambar(self, fill, outline, fn):
        """Jalankan fn(draw) di kanvas; kalau warnanya tembus pandang, gambar di lapisan
        sementara lalu digabungkan (alpha composite)."""
        transparan = (fill is not None and len(fill) == 4 and fill[3] < 255) or \
                     (outline is not None and len(outline) == 4 and outline[3] < 255)
        if transparan:
            lapis = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
            fn(ImageDraw.Draw(lapis))
            self.img.alpha_composite(lapis)
            self.d = ImageDraw.Draw(self.img)
        else:
            fn(self.d)

    def elips(self, box, fill, outline=OUTLINE, lebar=2):
        self._gambar(fill, outline, lambda d: d.ellipse(
            self._b(box), fill=fill, outline=outline, width=lebar * S if outline else 0))

    def kotak(self, box, fill, outline=OUTLINE, lebar=2, radius=0):
        self._gambar(fill, outline, lambda d: d.rounded_rectangle(
            self._b(box), radius=radius * S, fill=fill, outline=outline, width=lebar * S if outline else 0))

    def poligon(self, titik, fill, outline=OUTLINE, lebar=2):
        pts = [(x * S, y * S) for x, y in titik]
        self._gambar(fill, outline, lambda d: d.polygon(
            pts, fill=fill, outline=outline, width=lebar * S if outline else 0))

    def garis(self, titik, fill=OUTLINE, lebar=2):
        pts = [(x * S, y * S) for x, y in titik]
        self._gambar(fill, None, lambda d: d.line(pts, fill=fill, width=lebar * S, joint="curve"))

    def busur(self, box, mulai, akhir, fill=OUTLINE, lebar=2):
        self._gambar(fill, None, lambda d: d.arc(self._b(box), mulai, akhir, fill=fill, width=lebar * S))

    def teks(self, xy, s, ukuran, fill=PUTIH, outline=None):
        f = font(ukuran * S)
        x, y = xy[0] * S, xy[1] * S
        if outline:
            self.d.text((x, y), s, font=f, fill=outline, anchor="mm", stroke_width=2 * S, stroke_fill=outline)
        self.d.text((x, y), s, font=f, fill=fill, anchor="mm")

    def hamzah(self, xy, ukuran, fill=HITAM):
        """Mata berbentuk huruf hamzah (ء) -- ide anak-anak."""
        f = font_arab(int(ukuran * S))
        self.d.text((xy[0] * S, xy[1] * S), "\u0621", font=f, fill=fill, anchor="mm")

    def simpan(self, nama):
        kecil = self.img.resize((self.w, self.h), Image.LANCZOS)
        kecil.save(OUT / nama)
        print("  ", nama)


# =====================================================================
# PETUALANG  (badan 64x64, kepala 56x56)  -- kepala terpisah dari badan
# =====================================================================
def petualang_badan(nama, kaki_kiri=0, kaki_kanan=0, lengan=0):
    k = Kanvas(64, 64)
    # kaki (belakang badan)
    k.kotak([20, 38 + kaki_kiri, 30, 58 + kaki_kiri], KULIT, radius=3)
    k.kotak([34, 38 + kaki_kanan, 44, 58 + kaki_kanan], KULIT, radius=3)
    # sepatu
    k.kotak([18, 54 + kaki_kiri, 31, 62 + kaki_kiri], SEPATU, radius=3)
    k.kotak([33, 54 + kaki_kanan, 46, 62 + kaki_kanan], SEPATU, radius=3)
    # celana pendek
    k.kotak([17, 30, 47, 44], CELANA, radius=4)
    # badan / baju
    k.kotak([16, 8, 48, 36], BAJU, radius=8)
    # rompi
    k.kotak([16, 8, 26, 36], BAJU_GELAP, outline=None, radius=6)
    k.kotak([38, 8, 48, 36], BAJU_GELAP, outline=None, radius=6)
    k.kotak([16, 8, 48, 36], None, radius=8)  # garis tepi ulang (tanpa isi)
    # kancing
    k.elips([30, 16, 34, 20], OUTLINE, outline=None)
    k.elips([30, 24, 34, 28], OUTLINE, outline=None)
    # lengan
    k.kotak([6, 12 + lengan, 16, 34 + lengan], BAJU, radius=5)
    k.kotak([48, 12 - lengan, 58, 34 - lengan], BAJU, radius=5)
    k.elips([6, 30 + lengan, 16, 40 + lengan], KULIT)   # tangan
    k.elips([48, 30 - lengan, 58, 40 - lengan], KULIT)
    # tas ransel kecil (tali)
    k.garis([(22, 9), (22, 30)], fill=KERANJANG_GELAP, lebar=2)
    k.garis([(42, 9), (42, 30)], fill=KERANJANG_GELAP, lebar=2)
    k.simpan(nama)


def petualang_kepala(nama, kaget=False):
    k = Kanvas(56, 56)
    # rambut belakang
    k.elips([8, 12, 48, 50], RAMBUT)
    # wajah
    k.elips([10, 16, 46, 52], KULIT)
    # telinga
    k.elips([6, 30, 14, 40], KULIT)
    k.elips([42, 30, 50, 40], KULIT)
    # poni
    k.poligon([(12, 26), (18, 18), (26, 24), (32, 17), (40, 24), (44, 27), (44, 20), (30, 12), (14, 18)], RAMBUT)
    # topi petualang (safari)
    k.elips([2, 12, 54, 24], TOPI)                    # pinggiran topi
    k.kotak([12, 2, 44, 18], TOPI, radius=8)          # mahkota topi
    k.kotak([12, 12, 44, 16], TOPI_GELAP, outline=None)  # pita topi
    k.elips([2, 12, 54, 24], None)            # tepi pinggiran di atas mahkota
    # mata
    if kaget:
        k.elips([17, 29, 27, 41], PUTIH)              # mata melotot
        k.elips([29, 29, 39, 41], PUTIH)
        k.hamzah((22, 35), 22)                        # mata = huruf hamzah
        k.hamzah((34, 35), 22)
        k.elips([24, 42, 32, 49], HITAM)              # mulut "O"
        # alis kaget
        k.garis([(17, 27), (26, 25)], lebar=2)
        k.garis([(30, 25), (39, 27)], lebar=2)
    else:
        k.hamzah((21, 34), 26)                            # mata = huruf hamzah (ء)
        k.hamzah((35, 34), 26)
        k.busur([22, 36, 34, 47], 15, 165, lebar=2)      # senyum
        k.elips([13, 40, 19, 44], MERAH_PIPI, outline=None)
        k.elips([37, 40, 43, 44], MERAH_PIPI, outline=None)
    k.simpan(nama)


def petualang_telur(nama):
    """Petualang yang berubah jadi telur (badan+kepala jadi satu telur bertopi)."""
    k = Kanvas(64, 72)
    k.elips([8, 14, 56, 70], TELUR)
    k.elips([12, 26, 24, 40], TELUR_GELAP, outline=None)  # bayangan
    # bintik
    for (x, y) in [(20, 52), (40, 58), (44, 34), (26, 22)]:
        k.elips([x, y, x + 5, y + 4], TELUR_BINTIK, outline=None)
    # topi masih dipakai :)
    k.elips([6, 14, 58, 26], TOPI)
    k.kotak([16, 4, 48, 20], TOPI, radius=8)
    k.kotak([16, 14, 48, 18], TOPI_GELAP, outline=None)
    k.elips([6, 14, 58, 26], None)
    # wajah sedih
    k.hamzah((24, 40), 26)                          # mata hamzah (sedih)
    k.hamzah((40, 40), 26)
    k.busur([25, 50, 39, 60], 195, 345, lebar=2)  # mulut sedih
    # air mata
    k.elips([18, 44, 22, 50], (150, 200, 255, 255), outline=None)
    k.simpan(nama)


# =====================================================================
# KELINCI (badan 64x72, kepala 72x72) -- kepala terpisah dari badan
# =====================================================================
def kelinci_badan(nama):
    k = Kanvas(64, 72)
    # ekor
    k.elips([44, 44, 62, 62], KELINCI)
    # kaki belakang
    k.elips([6, 46, 30, 66], KELINCI)
    k.elips([34, 46, 58, 66], KELINCI)
    # badan
    k.elips([12, 10, 52, 62], KELINCI)
    k.elips([20, 24, 44, 56], KELINCI_GELAP, outline=None)  # perut
    # tangan/lengan depan
    k.elips([8, 30, 22, 44], KELINCI)
    k.elips([42, 30, 56, 44], KELINCI)
    # jari kaki
    for x in [10, 16, 22]:
        k.garis([(x, 62), (x, 66)], lebar=1)
    for x in [38, 44, 50]:
        k.garis([(x, 62), (x, 66)], lebar=1)
    k.simpan(nama)


def kelinci_kepala(nama, marah=False):
    k = Kanvas(72, 72)
    # telinga
    for (x0, x1) in [(16, 30), (42, 56)]:
        k.elips([x0, 0, x1, 40], KELINCI)
        k.elips([x0 + 4, 5, x1 - 4, 34], PINK, outline=None)
    # kepala
    k.elips([8, 26, 64, 70], KELINCI)
    # pipi
    k.elips([12, 46, 34, 64], KELINCI)
    k.elips([38, 46, 60, 64], KELINCI)
    # hidung
    k.poligon([(31, 50), (41, 50), (36, 56)], PINK)
    # kumis
    for dy in (-2, 3):
        k.garis([(6, 54 + dy), (20, 52 + dy)], lebar=1)
        k.garis([(52, 52 + dy), (66, 54 + dy)], lebar=1)
    # gigi
    k.kotak([32, 58, 36, 64], PUTIH, lebar=1)
    k.kotak([36, 58, 40, 64], PUTIH, lebar=1)
    if marah:
        # mata sipit + alis miring
        k.hamzah((25, 45), 26)                        # mata hamzah
        k.hamzah((47, 45), 26)
        k.garis([(16, 36), (30, 42)], lebar=3)
        k.garis([(56, 36), (42, 42)], lebar=3)
        # pipi merah
        k.elips([12, 52, 22, 58], (255, 110, 110, 220), outline=None)
        k.elips([50, 52, 60, 58], (255, 110, 110, 220), outline=None)
        # mulut cemberut kecil
        k.busur([28, 60, 44, 70], 200, 340, lebar=2)
        # tanda marah (uap) di dahi
        k.garis([(30, 30), (36, 24), (42, 30)], fill=(220, 60, 60, 255), lebar=2)
    else:
        k.hamzah((25, 43), 30)                        # mata hamzah (ء)
        k.hamzah((47, 43), 30)
        k.elips([12, 52, 22, 58], MERAH_PIPI, outline=None)
        k.elips([50, 52, 60, 58], MERAH_PIPI, outline=None)
    k.simpan(nama)


# =====================================================================
# TELUR (48x60): utuh + 3 tahap pecah
# =====================================================================
def telur(nama, tahap=0):
    k = Kanvas(48, 60)
    k.elips([4, 4, 44, 58], TELUR)
    k.elips([8, 14, 18, 30], PUTIH, outline=None)          # kilau
    for (x, y) in [(28, 16), (14, 40), (32, 44), (22, 30)]:
        k.elips([x, y, x + 5, y + 4], TELUR_BINTIK, outline=None)
    if tahap >= 1:
        k.garis([(20, 12), (24, 20), (18, 26), (26, 34)], lebar=2)
    if tahap >= 2:
        k.garis([(26, 34), (20, 42), (30, 50)], lebar=2)
        k.garis([(24, 20), (32, 24), (36, 32)], lebar=2)
        k.garis([(18, 26), (10, 30)], lebar=2)
    if tahap >= 3:
        # bagian atas cangkang lepas / terbuka
        k.elips([4, 4, 44, 58], (0, 0, 0, 0), outline=None)
        k2 = k  # gambar ulang: bawah cangkang zig-zag + kuning telur mengintip
        k.img.paste((0, 0, 0, 0), (0, 0, k.img.width, k.img.height))
        # cangkang bawah dengan tepi zig-zag
        titik = [(4, 34), (10, 26), (16, 34), (22, 24), (28, 34), (34, 26), (40, 34), (44, 36),
                 (44, 46), (36, 57), (24, 59), (12, 57), (4, 46)]
        k.poligon(titik, TELUR)
        # cangkang atas terlepas (miring) di kanan atas
        k.poligon([(28, 4), (44, 12), (46, 24), (36, 20), (30, 12)], TELUR)
        # sinar keluar (isi telur = kejutan)
        for a in range(0, 360, 45):
            x = 24 + 22 * math.cos(math.radians(a))
            y = 30 + 22 * math.sin(math.radians(a))
            k.garis([(24 + 12 * math.cos(math.radians(a)), 30 + 12 * math.sin(math.radians(a))), (x, y)],
                    fill=(255, 220, 90, 255), lebar=2)
        k.elips([16, 22, 32, 38], (255, 225, 100, 255))
    k.simpan(nama)


# =====================================================================
# KERANJANG (64x56)
# =====================================================================
def keranjang(nama):
    k = Kanvas(64, 56)
    k.busur([12, 2, 52, 40], 200, 340, fill=OUTLINE, lebar=4)      # pegangan (tepi)
    k.busur([12, 2, 52, 40], 200, 340, fill=KERANJANG, lebar=2)    # pegangan
    k.poligon([(4, 20), (60, 20), (54, 54), (10, 54)], KERANJANG)  # badan keranjang
    for y in [28, 36, 44]:
        k.garis([(7, y), (57, y)], fill=KERANJANG_GELAP, lebar=1)
    for x in [16, 26, 36, 46]:
        k.garis([(x, 21), (x - 2, 53)], fill=KERANJANG_GELAP, lebar=1)
    k.kotak([2, 16, 62, 24], KERANJANG_GELAP, radius=3)            # bibir keranjang
    k.simpan(nama)


# =====================================================================
# HUTAN: rumput (tile 128x128, mulus), pohon, semak, bunga, batu
# =====================================================================
def rumput(nama):
    random.seed(7)
    k = Kanvas(128, 128)
    k.kotak([0, 0, 128, 128], RUMPUT, outline=None)
    for _ in range(140):
        x, y = random.uniform(0, 128), random.uniform(0, 128)
        warna = random.choice([RUMPUT_TERANG, RUMPUT_GELAP])
        h = random.uniform(4, 9)
        # digambar 4x dengan offset agar tile mulus (wrap-around)
        for dx in (0, 128, -128):
            for dy in (0, 128, -128):
                k.garis([(x + dx, y + dy), (x + dx + 1.5, y + dy - h)], fill=warna, lebar=1)
    k.simpan(nama)


def pohon(nama):
    k = Kanvas(128, 160)
    k.elips([44, 128, 84, 144], (0, 0, 0, 60), outline=None)          # bayangan
    k.kotak([54, 90, 74, 140], BATANG, radius=5)
    k.elips([12, 30, 76, 100], DAUN)
    k.elips([52, 20, 116, 90], DAUN)
    k.elips([28, 4, 100, 70], DAUN_TERANG)
    k.elips([24, 50, 104, 110], DAUN)
    k.elips([40, 14, 88, 60], DAUN_TERANG, outline=None)
    for (x, y) in [(40, 70), (80, 60), (60, 90), (95, 85)]:
        k.elips([x, y, x + 8, y + 8], (230, 80, 80, 255))  # buah merah
    k.simpan(nama)


def semak(nama):
    k = Kanvas(96, 64)
    k.elips([20, 52, 76, 62], (0, 0, 0, 60), outline=None)
    k.elips([2, 20, 50, 60], DAUN)
    k.elips([46, 20, 94, 60], DAUN)
    k.elips([22, 4, 74, 56], DAUN_TERANG)
    k.simpan(nama)


def bunga(nama, warna):
    k = Kanvas(32, 32)
    k.garis([(16, 18), (16, 30)], fill=DAUN_GELAP, lebar=2)
    for a in range(0, 360, 72):
        x = 16 + 8 * math.cos(math.radians(a - 90))
        y = 13 + 8 * math.sin(math.radians(a - 90))
        k.elips([x - 6, y - 6, x + 6, y + 6], warna, lebar=1)
    k.elips([11, 8, 21, 18], (255, 225, 90, 255), lebar=1)
    k.simpan(nama)


def batu(nama):
    k = Kanvas(48, 36)
    k.elips([2, 8, 46, 34], (150, 150, 160, 255))
    k.elips([10, 12, 30, 24], (190, 190, 200, 255), outline=None)
    k.simpan(nama)


# =====================================================================
# UI: panel soal, tombol
# =====================================================================
def panel(nama, w=900, h=470):
    k = Kanvas(w, h)
    k.kotak([4, 4, w - 4, h - 4], (255, 250, 235, 255), outline=(120, 80, 40, 255), lebar=4, radius=28)
    k.kotak([16, 16, w - 16, h - 16], None, outline=(220, 190, 140, 255), lebar=2, radius=20)
    k.simpan(nama)


def tombol(nama, teks, warna, warna_gelap, w=220, h=90, ukuran=34):
    k = Kanvas(w, h)
    k.kotak([4, 8, w - 4, h - 2], warna_gelap, radius=22)      # bayangan bawah
    k.kotak([4, 2, w - 4, h - 10], warna, radius=22)
    k.kotak([16, 8, w - 16, h / 2 - 8], (255, 255, 255, 60), outline=None, radius=14)  # kilau
    if teks:
        k.teks((w / 2, h / 2 - 5), teks, ukuran, fill=PUTIH, outline=(0, 0, 0, 120))
    k.simpan(nama)


def asap(nama, tahap):
    """Efek asap/puff saat petualang berubah jadi telur (3 tahap: kecil -> besar -> pudar)."""
    k = Kanvas(96, 96)
    r = [16, 30, 40][tahap]
    alpha = [230, 200, 110][tahap]
    warna = (250, 250, 250, alpha)
    tepi = (200, 200, 210, alpha)
    for a in range(0, 360, 60):
        x = 48 + r * 0.7 * math.cos(math.radians(a))
        y = 48 + r * 0.7 * math.sin(math.radians(a))
        k.elips([x - r * 0.6, y - r * 0.6, x + r * 0.6, y + r * 0.6], warna, outline=tepi, lebar=1)
    k.elips([48 - r * 0.8, 48 - r * 0.8, 48 + r * 0.8, 48 + r * 0.8], warna, outline=None)
    k.simpan(nama)


# =====================================================================
# BONEKA KELINCI (koleksi): 6 warna (per wazan) x 4 tingkat (polos, pita, topi, mahkota)
# =====================================================================
WARNA_BONEKA = {
    1: (250, 245, 235, 255),   # krem
    2: (255, 190, 205, 255),   # merah muda
    3: (180, 215, 250, 255),   # biru muda
    4: (190, 235, 180, 255),   # hijau muda
    5: (255, 235, 150, 255),   # kuning
    6: (215, 195, 245, 255),   # ungu muda
}


def boneka(nama, bab, tingkat):
    w = WARNA_BONEKA[bab]
    gelap = tuple(max(0, c - 35) for c in w[:3]) + (255,)
    k = Kanvas(96, 120)
    # telinga
    for (x0, x1) in [(24, 40), (56, 72)]:
        k.elips([x0, 4, x1, 50], w)
        k.elips([x0 + 4, 10, x1 - 4, 44], PINK, outline=None)
    # badan (bulat, boneka duduk)
    k.elips([14, 62, 82, 118], w)
    k.elips([30, 78, 66, 112], gelap, outline=None)  # perut
    # kaki
    k.elips([12, 98, 40, 118], w)
    k.elips([56, 98, 84, 118], w)
    # kepala
    k.elips([16, 30, 80, 84], w)
    # mata hamzah + hidung + pipi + jahitan boneka
    k.hamzah((36, 54), 22)
    k.hamzah((60, 54), 22)
    k.poligon([(43, 62), (53, 62), (48, 68)], PINK)
    k.elips([22, 60, 32, 66], MERAH_PIPI, outline=None)
    k.elips([64, 60, 74, 66], MERAH_PIPI, outline=None)
    k.garis([(48, 68), (48, 74)], lebar=1)
    k.garis([(42, 76), (54, 76)], fill=OUTLINE, lebar=1)  # mulut jahit
    # tingkat
    if tingkat >= 2:   # pita di leher
        k.poligon([(48, 82), (34, 74), (34, 90)], (230, 60, 90, 255))
        k.poligon([(48, 82), (62, 74), (62, 90)], (230, 60, 90, 255))
        k.elips([44, 78, 52, 86], (250, 90, 120, 255))
    if tingkat == 3:   # topi pesta
        k.poligon([(48, 2), (34, 34), (62, 34)], (90, 160, 240, 255))
        k.elips([44, 0, 52, 8], (255, 220, 80, 255))
        for y in (16, 26):
            k.garis([(48 - (y - 2) * 0.42, y), (48 + (y - 2) * 0.42, y)], fill=(255, 255, 255, 255), lebar=1)
    if tingkat >= 4:   # mahkota emas menggantikan topi
        k.poligon([(30, 34), (30, 12), (39, 24), (48, 6), (57, 24), (66, 12), (66, 34)], (255, 205, 60, 255))
        for x in (30, 48, 66):
            k.elips([x - 3, 8 if x == 48 else 12, x + 3, 14 if x == 48 else 18], (240, 80, 90, 255), lebar=1)
    k.simpan(nama)


def boneka_kosong(nama):
    k = Kanvas(96, 120)
    abu = (200, 200, 200, 255)
    for (x0, x1) in [(24, 40), (56, 72)]:
        k.elips([x0, 4, x1, 50], abu, outline=(160, 160, 160, 255))
    k.elips([14, 62, 82, 118], abu, outline=(160, 160, 160, 255))
    k.elips([16, 30, 80, 84], abu, outline=(160, 160, 160, 255))
    k.teks((48, 60), "?", 40, fill=(120, 120, 120, 255))
    k.simpan(nama)


def tanda(nama, teks, warna):
    """Papan kayu bertiang dengan tulisan (START / FINISH)."""
    k = Kanvas(96, 96)
    k.kotak([44, 40, 52, 92], BATANG, radius=2)
    k.kotak([4, 6, 92, 46], warna, radius=8, lebar=3)
    k.teks((48, 26), teks, 22, fill=PUTIH, outline=(0, 0, 0, 140))
    k.simpan(nama)


def panah(nama):
    k = Kanvas(56, 40)
    k.poligon([(2, 12), (30, 12), (30, 2), (54, 20), (30, 38), (30, 28), (2, 28)], (255, 220, 80, 255), lebar=2)
    k.simpan(nama)


# =====================================================================
# PETA MINI (minimap) di HUD
# =====================================================================
def peta_sel(nama, warna):
    k = Kanvas(8, 8)
    k.kotak([0, 0, 8, 8], warna, outline=None)
    k.simpan(nama)


def peta_titik(nama, warna, ukuran=10):
    k = Kanvas(ukuran, ukuran)
    k.elips([0.5, 0.5, ukuran - 0.5, ukuran - 0.5], warna, outline=(40, 30, 20, 255), lebar=1)
    k.simpan(nama)


def panel_peta(nama, w=176, h=128):
    k = Kanvas(w, h)
    k.kotak([1, 1, w - 1, h - 1], (60, 45, 30, 230), outline=(200, 160, 100, 255), lebar=3, radius=6)
    k.simpan(nama)


def ikon(nama):
    k = Kanvas(512, 512)
    k.kotak([0, 0, 512, 512], RUMPUT, outline=None, radius=90)
    k.elips([116, 60, 396, 452], TELUR, lebar=8)
    k.elips([150, 120, 210, 220], PUTIH, outline=None)
    for (x, y) in [(300, 150), (200, 320), (320, 360), (250, 250)]:
        k.elips([x, y, x + 34, y + 28], TELUR_BINTIK, outline=None)
    k.garis([(230, 90), (260, 150), (215, 200), (270, 260)], lebar=8)
    k.simpan(nama)


if __name__ == "__main__":
    print("Membuat aset di", OUT)
    # Petualang: badan (diam + 4 frame jalan) & kepala (normal, kaget) & bentuk telur
    petualang_badan("petualang_badan_diam.png")
    petualang_badan("petualang_badan_jalan1.png", kaki_kiri=-4, kaki_kanan=2, lengan=3)
    petualang_badan("petualang_badan_jalan2.png", kaki_kiri=0, kaki_kanan=0, lengan=0)
    petualang_badan("petualang_badan_jalan3.png", kaki_kiri=2, kaki_kanan=-4, lengan=-3)
    petualang_badan("petualang_badan_jalan4.png", kaki_kiri=0, kaki_kanan=0, lengan=0)
    petualang_kepala("petualang_kepala_normal.png")
    petualang_kepala("petualang_kepala_kaget.png", kaget=True)
    petualang_telur("petualang_telur.png")
    # Kelinci
    kelinci_badan("kelinci_badan.png")
    kelinci_kepala("kelinci_kepala_biasa.png")
    kelinci_kepala("kelinci_kepala_marah.png", marah=True)
    # Telur
    telur("telur_utuh.png", 0)
    telur("telur_pecah1.png", 1)
    telur("telur_pecah2.png", 2)
    telur("telur_pecah3.png", 3)
    keranjang("keranjang.png")
    # Hutan
    rumput("rumput.png")
    pohon("pohon.png")
    semak("semak.png")
    bunga("bunga_merah.png", (240, 90, 110, 255))
    bunga("bunga_ungu.png", (170, 120, 230, 255))
    batu("batu.png")
    # UI
    panel("panel_soal.png")
    panel("panel_hasil.png", w=900, h=190)
    tombol("tombol_ya.png", "YA", (80, 190, 100, 255), (50, 140, 70, 255))
    tombol("tombol_tidak.png", "TIDAK", (230, 90, 90, 255), (170, 55, 55, 255))
    tombol("tombol_bab.png", "", (255, 170, 60, 255), (200, 120, 30, 255), w=360, h=100)
    tombol("tombol_lagi.png", "MAIN LAGI", (80, 150, 230, 255), (45, 100, 180, 255), w=320, h=96, ukuran=32)
    for bab in range(1, 7):
        for tingkat in range(1, 5):
            boneka(f"boneka_b{bab}_t{tingkat}.png", bab, tingkat)
    boneka_kosong("boneka_kosong.png")
    tanda("tanda_start.png", "START", (80, 170, 90, 255))
    tanda("tanda_finish.png", "FINISH", (230, 90, 70, 255))
    panah("panah.png")
    tombol("tombol_rak.png", "RAK BONEKA", (200, 120, 220, 255), (150, 80, 170, 255), w=320, h=90, ukuran=28)
    tombol("tombol_kembali.png", "KEMBALI", (120, 120, 130, 255), (80, 80, 90, 255), w=260, h=86, ukuran=28)
    peta_sel("peta_jalur.png", (150, 210, 110, 255))
    peta_sel("peta_pohon.png", (40, 90, 45, 255))
    peta_titik("peta_pemain.png", (255, 80, 80, 255), 10)
    peta_titik("peta_telur.png", (255, 240, 150, 255), 7)
    peta_titik("peta_start.png", (80, 200, 100, 255), 12)
    peta_titik("peta_finish.png", (240, 80, 60, 255), 12)
    panel_peta("panel_peta.png")
    asap("asap1.png", 0)
    asap("asap2.png", 1)
    asap("asap3.png", 2)
    ikon("ikon.png")
    print("Selesai.")
