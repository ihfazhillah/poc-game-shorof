#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Membuat file proyek GDevelop `game.json` untuk "Telur Wazan".

Jalankan:  python3 tools/buat_game.py
Hasil:     game.json  (buka di GDevelop 5: File > Open > pilih game.json)

PERHATIAN: Setelah Anda mengubah proyek di GDevelop, JANGAN jalankan skrip ini lagi
(karena game.json akan ditimpa dari awal). Skrip ini hanya "titik awal".

Isi proyek dijelaskan di PANDUAN-GDEVELOP.md.
"""
import json, sys, uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from soal import daftar_soal, NAMA_BAB  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEBAR, TINGGI = 1280, 720          # ukuran layar game
DUNIA_W, DUNIA_H = 2000, 1400      # ukuran hutan (lebih besar dari layar, kamera mengikuti)

FONT_ARAB = "assets/fonts/Amiri-Regular.ttf"
FONT_ARAB_TEBAL = "assets/fonts/Amiri-Bold.ttf"
FONT_LATIN = "assets/fonts/Comfortaa-Bold.otf"

# ---------------------------------------------------------------------------
# Pengukur lebar teks (memakai Pillow) supaya teks bisa diletakkan di tengah
# ---------------------------------------------------------------------------
try:
    from PIL import ImageFont

    def lebar_teks(teks, font_path, ukuran):
        f = ImageFont.truetype(str(ROOT / font_path), ukuran)
        return f.getlength(teks)
except Exception:  # pragma: no cover
    def lebar_teks(teks, font_path, ukuran):
        return len(teks) * ukuran * 0.55


def tengah_x(teks, font_path, ukuran, pusat=LEBAR / 2):
    return round(pusat - lebar_teks(teks, font_path, ukuran) / 2)


# ---------------------------------------------------------------------------
# Pembantu untuk menulis JSON GDevelop
# ---------------------------------------------------------------------------
def uid():
    return str(uuid.uuid4())


def C(tipe, *params, inverted=False):
    """Kondisi."""
    return {"type": {"inverted": inverted, "value": tipe}, "parameters": list(params), "subInstructions": []}


def A(tipe, *params):
    """Aksi."""
    return {"type": {"inverted": False, "value": tipe}, "parameters": list(params), "subInstructions": []}


def E(conds=(), acts=(), sub=()):
    """Event standar: JIKA kondisi MAKA aksi (+ sub-event)."""
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::Standard",
            "conditions": list(conds), "actions": list(acts), "events": list(sub)}


def komentar(teks):
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::Comment",
            "color": {"b": 109, "g": 230, "r": 255, "textB": 0, "textG": 0, "textR": 0},
            "comment": teks, "comment2": ""}


def grup(nama, events, warna=(74, 176, 228)):
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::Group",
            "colorR": warna[0], "colorG": warna[1], "colorB": warna[2], "creationTime": 0,
            "name": nama, "source": "", "events": list(events)}


def ulangi(ekspresi, conds=(), acts=(), sub=()):
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::Repeat",
            "repeatExpression": str(ekspresi), "conditions": list(conds), "actions": list(acts), "events": list(sub)}


def untuk_setiap(objek, conds=(), acts=(), sub=()):
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::ForEach",
            "object": objek, "conditions": list(conds), "actions": list(acts), "events": list(sub)}


def js(kode):
    return {"disabled": False, "folded": False, "type": "BuiltinCommonInstructions::JsCode",
            "inlineCode": kode, "parameterObjects": "", "useStrict": True, "eventsSheetExpanded": True}


def s(teks):
    """Bungkus teks jadi ekspresi string GDevelop: "..." """
    return '"' + teks.replace('"', '\\"') + '"'


# ---- variabel ----
def var_angka(nama, nilai):
    return {"name": nama, "type": "number", "value": nilai}


def var_teks(nama, nilai):
    return {"name": nama, "type": "string", "value": nilai}


def var_array_teks(nama, daftar):
    return {"name": nama, "type": "array", "children": [{"type": "string", "value": t} for t in daftar]}


# ---- objek ----
def frame(gambar):
    return {"hasCustomCollisionMask": False, "image": gambar, "points": [],
            "originPoint": {"name": "origine", "x": 0, "y": 0},
            "centerPoint": {"automatic": True, "name": "centre", "x": 0, "y": 0},
            "customCollisionMask": []}


def sprite(nama, animasi, behaviors=(), variables=()):
    """animasi: list of (namaAnimasi, [gambar...], loop, waktuAntarFrame)"""
    return {
        "adaptCollisionMaskAutomatically": True, "assetStoreId": "", "name": nama, "type": "Sprite",
        "updateIfNotVisible": False, "variables": list(variables), "effects": [], "behaviors": list(behaviors),
        "animations": [
            {"name": n, "useMultipleDirections": False,
             "directions": [{"looping": loop, "timeBetweenFrames": t, "sprites": [frame(g) for g in gambar]}]}
            for (n, gambar, loop, t) in animasi
        ],
    }


def teks(nama, isi, ukuran, font="", warna=(40, 30, 20), tebal=False, rata="left",
         garis_tepi=None, tebal_tepi=3, behaviors=(), variables=()):
    r, g, b = warna
    konten = {
        "bold": tebal, "isOutlineEnabled": garis_tepi is not None, "isShadowEnabled": False, "italic": False,
        "outlineColor": "%d;%d;%d" % (garis_tepi or (0, 0, 0)), "outlineThickness": tebal_tepi,
        "shadowAngle": 90, "shadowBlurRadius": 2, "shadowColor": "0;0;0", "shadowDistance": 4, "shadowOpacity": 127,
        "smoothed": True, "underlined": False, "text": isi, "font": font, "textAlignment": rata,
        "verticalTextAlignment": "top", "characterSize": ukuran, "lineHeight": 0, "color": "%d;%d;%d" % (r, g, b),
    }
    return {"assetStoreId": "", "bold": tebal, "italic": False, "name": nama, "smoothed": True,
            "type": "TextObject::Text", "underlined": False, "variables": list(variables), "effects": [],
            "behaviors": list(behaviors), "string": isi, "font": font, "textAlignment": rata,
            "characterSize": ukuran, "color": {"b": b, "g": g, "r": r}, "content": konten}


def tiled(nama, gambar, w, h):
    return {"assetStoreId": "", "height": h, "name": nama, "texture": gambar,
            "type": "TiledSpriteObject::TiledSprite", "width": w, "variables": [], "effects": [], "behaviors": []}


def topdown(kecepatan=260):
    return {"name": "TopDownMovement", "type": "TopDownMovementBehavior::TopDownMovementBehavior",
            "acceleration": 1200, "allowDiagonals": True, "angleOffset": 0, "angularMaxSpeed": 180,
            "customIsometryAngle": 30, "deceleration": 1600, "ignoreDefaultControls": False,
            "maxSpeed": kecepatan, "movementAngleOffset": 0, "rotateObject": False, "viewpoint": "TopDown"}


def instance(nama, x, y, z=0, layer="", w=None, h=None, variabel=None):
    d = {"angle": 0, "customSize": w is not None, "height": h or 0, "keepRatio": True, "layer": layer,
         "locked": False, "name": nama, "persistentUuid": uid(), "width": w or 0, "x": x, "y": y, "zOrder": z,
         "numberProperties": [], "stringProperties": [], "initialVariables": []}
    if variabel:
        for k, v in variabel.items():
            d["initialVariables"].append(var_angka(k, v) if isinstance(v, (int, float)) else var_teks(k, v))
    return d


def layer(nama, terlihat=True):
    return {"ambientLightColorB": 200, "ambientLightColorG": 200, "ambientLightColorR": 200,
            "camera3DFarPlaneDistance": 10000, "camera3DFieldOfView": 45, "camera3DNearPlaneDistance": 3,
            "cameraType": "", "followBaseLayerCamera": False, "isLightingLayer": False, "isLocked": False,
            "name": nama, "renderingType": "", "visibility": terlihat,
            "cameras": [{"defaultSize": True, "defaultViewport": True, "height": 0, "viewportBottom": 1,
                         "viewportLeft": 0, "viewportRight": 1, "viewportTop": 0, "width": 0}],
            "effects": []}


def scene(nama, objects, instances, events, variables=(), layers=None, groups=(), latar=(120, 184, 82)):
    r, g, b = latar
    return {
        "b": b, "disableInputWhenNotFocused": True, "mangledName": nama, "name": nama, "r": r,
        "standardSortMethod": True, "stopSoundsOnStartup": True, "title": "", "v": g,
        "uiSettings": {"grid": False, "gridType": "rectangular", "gridWidth": 32, "gridHeight": 32,
                       "gridOffsetX": 0, "gridOffsetY": 0, "gridColor": 10401023, "gridAlpha": 0.8,
                       "snap": False, "zoomFactor": 0.5, "windowMask": True},
        "objectsGroups": [{"name": n, "objects": [{"name": o} for o in objs]} for (n, objs) in groups],
        "variables": list(variables),
        "instances": list(instances),
        "objects": list(objects),
        "objectsFolderStructure": {"folderName": "__ROOT", "children": [{"objectName": o["name"]} for o in objects]},
        "events": list(events),
        "layers": layers or [layer("")],
        "behaviorsSharedData": [
            {"name": "TopDownMovement", "type": "TopDownMovementBehavior::TopDownMovementBehavior"},
            {"name": "Tween", "type": "Tween::TweenBehavior"},
        ],
    }


# ---------------------------------------------------------------------------
# RESOURCES (gambar, suara, font)
# ---------------------------------------------------------------------------
def kumpulkan_resources():
    res = []
    for p in sorted((ROOT / "assets").glob("*.png")):
        nama = "assets/" + p.name
        res.append({"alwaysLoaded": False, "file": nama, "kind": "image", "metadata": "",
                    "name": nama, "smoothed": True, "userAdded": True})
    for p in sorted((ROOT / "assets" / "fonts").glob("*.[ot]tf")):
        nama = "assets/fonts/" + p.name
        res.append({"file": nama, "kind": "font", "metadata": "", "name": nama, "userAdded": True})
    for sub in ("sfx", "suara", "soal"):
        for p in sorted((ROOT / "audio" / sub).glob("*.*")):
            if p.suffix.lower() not in (".mp3", ".wav", ".ogg"):
                continue
            nama = f"audio/{sub}/{p.name}"
            res.append({"file": nama, "kind": "audio", "metadata": "", "name": nama,
                        "preloadAsMusic": sub == "musik", "preloadAsSound": sub != "musik",
                        "preloadInCache": False, "userAdded": True})
    return res


# ---------------------------------------------------------------------------
# OBJEK GLOBAL (dipakai di semua scene)
# ---------------------------------------------------------------------------
def objek_global():
    return [
        sprite("Petualang", [
            ("diam", ["assets/petualang_badan_diam.png"], True, 0.2),
            ("jalan", ["assets/petualang_badan_jalan1.png", "assets/petualang_badan_jalan2.png",
                       "assets/petualang_badan_jalan3.png", "assets/petualang_badan_jalan4.png"], True, 0.12),
            ("telur", ["assets/petualang_telur.png"], True, 0.2),
        ], behaviors=[topdown()]),
        sprite("KepalaPetualang", [
            ("normal", ["assets/petualang_kepala_normal.png"], True, 0.2),
            ("kaget", ["assets/petualang_kepala_kaget.png"], True, 0.2),
        ]),
        sprite("Kelinci", [("diam", ["assets/kelinci_badan.png"], True, 0.2)]),
        sprite("KepalaKelinci", [
            ("biasa", ["assets/kelinci_kepala_biasa.png"], True, 0.2),
            ("marah", ["assets/kelinci_kepala_marah.png"], True, 0.2),
        ]),
        sprite("Telur", [
            ("utuh", ["assets/telur_utuh.png"], True, 0.2),
            ("pecah", ["assets/telur_pecah1.png", "assets/telur_pecah2.png", "assets/telur_pecah3.png"], False, 0.15),
        ], behaviors=[{"name": "Tween", "type": "Tween::TweenBehavior"}], variables=[var_angka("sel", -1)]),   # Tween: terbang ke keranjang; sel = nomor sel di peta
        # telur yang "terbang" ke keranjang (objek terpisah supaya tidak bisa ditabrak petualang lagi)
        sprite("TelurTerbang", [("utuh", ["assets/telur_utuh.png"], True, 0.2)], behaviors=[{"name": "Tween", "type": "Tween::TweenBehavior"}]),
        sprite("Keranjang", [("diam", ["assets/keranjang.png"], True, 0.2)], behaviors=[{"name": "Tween", "type": "Tween::TweenBehavior"}]),
        tiled("Rumput", "assets/rumput.png", 128, 128),
        sprite("Pohon", [("diam", ["assets/pohon.png"], True, 0.2)]),
        sprite("Semak", [("diam", ["assets/semak.png"], True, 0.2)]),
        sprite("Bunga", [("merah", ["assets/bunga_merah.png"], True, 0.2),
                         ("ungu", ["assets/bunga_ungu.png"], True, 0.2)]),
        sprite("Batu", [("diam", ["assets/batu.png"], True, 0.2)]),
        sprite("Asap", [("puff", ["assets/asap1.png", "assets/asap2.png", "assets/asap3.png"], False, 0.12)]),
        sprite("TandaStart", [("diam", ["assets/tanda_start.png"], True, 0.2)]),
        # objek peta mini (minimap) di HUD
        sprite("PanelPeta", [("diam", ["assets/panel_peta.png"], True, 0.2)]),
        sprite("PetaSel", [("jalur", ["assets/peta_jalur.png"], True, 0.2), ("pohon", ["assets/peta_pohon.png"], True, 0.2)]),
        sprite("PetaTelur", [("diam", ["assets/peta_telur.png"], True, 0.2)], variables=[var_angka("sel", 0)]),
        sprite("PetaPemain", [("diam", ["assets/peta_pemain.png"], True, 0.2)]),
        sprite("PetaStart", [("diam", ["assets/peta_start.png"], True, 0.2)]),
        sprite("PetaFinish", [("diam", ["assets/peta_finish.png"], True, 0.2)]),
        sprite("TandaFinish", [("diam", ["assets/tanda_finish.png"], True, 0.2)]),
        sprite("Panah", [("diam", ["assets/panah.png"], True, 0.2)]),
        # Boneka kelinci koleksi: animasi "b<bab>_t<tingkat>" (6 warna x 4 tingkat) + "kosong"
        sprite("Boneka", [("kosong", ["assets/boneka_kosong.png"], True, 0.2), ("b1_t1", ["assets/boneka_b1_t1.png"], True, 0.2), ("b1_t2", ["assets/boneka_b1_t2.png"], True, 0.2), ("b1_t3", ["assets/boneka_b1_t3.png"], True, 0.2), ("b1_t4", ["assets/boneka_b1_t4.png"], True, 0.2), ("b2_t1", ["assets/boneka_b2_t1.png"], True, 0.2), ("b2_t2", ["assets/boneka_b2_t2.png"], True, 0.2), ("b2_t3", ["assets/boneka_b2_t3.png"], True, 0.2), ("b2_t4", ["assets/boneka_b2_t4.png"], True, 0.2), ("b3_t1", ["assets/boneka_b3_t1.png"], True, 0.2), ("b3_t2", ["assets/boneka_b3_t2.png"], True, 0.2), ("b3_t3", ["assets/boneka_b3_t3.png"], True, 0.2), ("b3_t4", ["assets/boneka_b3_t4.png"], True, 0.2), ("b4_t1", ["assets/boneka_b4_t1.png"], True, 0.2), ("b4_t2", ["assets/boneka_b4_t2.png"], True, 0.2), ("b4_t3", ["assets/boneka_b4_t3.png"], True, 0.2), ("b4_t4", ["assets/boneka_b4_t4.png"], True, 0.2), ("b5_t1", ["assets/boneka_b5_t1.png"], True, 0.2), ("b5_t2", ["assets/boneka_b5_t2.png"], True, 0.2), ("b5_t3", ["assets/boneka_b5_t3.png"], True, 0.2), ("b5_t4", ["assets/boneka_b5_t4.png"], True, 0.2), ("b6_t1", ["assets/boneka_b6_t1.png"], True, 0.2), ("b6_t2", ["assets/boneka_b6_t2.png"], True, 0.2), ("b6_t3", ["assets/boneka_b6_t3.png"], True, 0.2), ("b6_t4", ["assets/boneka_b6_t4.png"], True, 0.2)], variables=[var_angka("bab", 1)],
               behaviors=[{"name": "Tween", "type": "Tween::TweenBehavior"}]),
    ]


# ---------------------------------------------------------------------------
# EVENT YANG DIPAKAI BERSAMA
# ---------------------------------------------------------------------------
def event_kepala_mengikuti_badan():
    """Kepala (objek terpisah) selalu ditempel di atas badan, setiap frame."""
    return grup("Kepala mengikuti badan (setiap frame)", [
        komentar("Kepala dan badan adalah objek TERPISAH. Setiap frame, posisi kepala diatur\n"
                 "mengikuti badan. Ubah angka +4 / -50 (petualang) dan -4 / -62 (kelinci) untuk menggeser kepala."),
        E([], [
            A("SetX", "KepalaPetualang", "=", "Petualang.X() + 4"),
            A("SetY", "KepalaPetualang", "=", "Petualang.Y() - 50"),
            A("SetX", "KepalaKelinci", "=", "Kelinci.X() - 4"),
            A("SetY", "KepalaKelinci", "=", "Kelinci.Y() - 62"),
        ]),
    ], warna=(150, 200, 120))


def event_kontrol_wasd():
    return grup("Kontrol tambahan: W A S D (panah sudah otomatis dari behavior)", [
        E([C("StringVariable", "Status", "=", s("jalan")), C("KeyFromTextPressed", "", s("w"))],
          [A("TopDownMovementBehavior::SimulateUpKey", "Petualang", "TopDownMovement")]),
        E([C("StringVariable", "Status", "=", s("jalan")), C("KeyFromTextPressed", "", s("s"))],
          [A("TopDownMovementBehavior::SimulateDownKey", "Petualang", "TopDownMovement")]),
        E([C("StringVariable", "Status", "=", s("jalan")), C("KeyFromTextPressed", "", s("a"))],
          [A("TopDownMovementBehavior::SimulateLeftKey", "Petualang", "TopDownMovement")]),
        E([C("StringVariable", "Status", "=", s("jalan")), C("KeyFromTextPressed", "", s("d"))],
          [A("TopDownMovementBehavior::SimulateRightKey", "Petualang", "TopDownMovement")]),
    ], warna=(200, 200, 120))


def event_animasi_petualang():
    return grup("Animasi petualang: diam / jalan", [
        E([C("StringVariable", "Status", "=", s("jalan")),
           C("TopDownMovementBehavior::IsMoving", "Petualang", "TopDownMovement")],
          [A("AnimatableCapability::AnimatableBehavior::SetName", "Petualang", "Animation", "=", s("jalan"))]),
        E([C("StringVariable", "Status", "=", s("jalan")),
           C("TopDownMovementBehavior::IsMoving", "Petualang", "TopDownMovement", inverted=True)],
          [A("AnimatableCapability::AnimatableBehavior::SetName", "Petualang", "Animation", "=", s("diam"))]),
    ], warna=(200, 200, 120))


# ---------------------------------------------------------------------------
# SCENE 1: MENU
# ---------------------------------------------------------------------------
def event_muat_koleksi():
    """Memuat koleksi boneka dari penyimpanan perangkat (Storage) ke variabel global Koleksi."""
    return grup("Muat koleksi boneka dari penyimpanan", [
        komentar("Koleksi boneka disimpan di perangkat dengan nama penyimpanan \"TelurWazan\", kunci \"koleksi\",\n"
                 "dalam bentuk teks JSON dari variabel global Koleksi (array 6 angka = jumlah boneka per wazan)."),
        E([C("SceneJustBegins", ""), C("GroupExists", s("TelurWazan"), s("koleksi"))], [
            A("ReadStringFromStorage", s("TelurWazan"), s("koleksi"), "", "KoleksiJSON"),
            A("JSONToVariableStructure2", "KoleksiJSON", "Koleksi"),
        ]),
    ], warna=(200, 180, 240))


def scene_menu():
    objects = [
        teks("Judul", "Telur Wazan", 84, FONT_LATIN, (255, 255, 255), tebal=True, garis_tepi=(90, 60, 30), tebal_tepi=5),
        teks("SubJudul", "Pilih wazan yang ingin dilatih:", 30, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 90, 40), tebal_tepi=3),
        sprite("TombolBab", [("normal", ["assets/tombol_bab.png"], True, 0.2)], variables=[var_angka("bab", 1)]),
        teks("LabelBab", "wazan", 44, FONT_ARAB_TEBAL, (60, 30, 10), tebal=True, rata="center", variables=[var_angka("bab", 1)]),
        sprite("TombolRak", [("normal", ["assets/tombol_rak.png"], True, 0.2)]),
        teks("Petunjuk", "Jalan: panah / WASD  •  Jawab: klik YA / TIDAK  •  Cari telur, lalu ke FINISH", 20, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 90, 40), tebal_tepi=2),
    ]
    inst = [instance("Rumput", 0, 0, 0, w=LEBAR, h=TINGGI)]
    for (x, y) in [(-10, 40), (1150, 20), (-30, 520), (1160, 500)]:
        inst.append(instance("Pohon", x, y, 2))
    for (x, y) in [(150, 640), (1000, 650)]:
        inst.append(instance("Semak", x, y, 1))
    for (x, y) in [(120, 200), (1130, 200), (200, 460), (1080, 430), (700, 690)]:
        inst.append(instance("Bunga", x, y, 1))
    inst.append(instance("Petualang", 120, 560, 10))
    inst.append(instance("KepalaPetualang", 124, 510, 11))
    inst.append(instance("Kelinci", 1090, 560, 10))
    inst.append(instance("KepalaKelinci", 1086, 498, 11))
    inst.append(instance("Telur", 220, 590, 5))
    inst.append(instance("Telur", 1030, 610, 5))
    inst.append(instance("Judul", tengah_x("Telur Wazan", FONT_LATIN, 84), 30, 5))
    inst.append(instance("SubJudul", tengah_x("Pilih wazan yang ingin dilatih:", FONT_LATIN, 30), 145, 5))
    petunjuk = "Jalan: panah / WASD  •  Jawab: klik YA / TIDAK  •  Cari telur, lalu ke FINISH"
    inst.append(instance("Petunjuk", tengah_x(petunjuk, FONT_LATIN, 20), 690, 5))
    posisi = [(250, 200), (670, 200), (250, 320), (670, 320), (250, 440), (670, 440)]
    for i, (x, y) in enumerate(posisi):
        bab = i + 1
        inst.append(instance("TombolBab", x, y, 5, variabel={"bab": bab}))
        lx = round(x + 180 - lebar_teks(NAMA_BAB[i], FONT_ARAB_TEBAL, 44) / 2)
        inst.append(instance("LabelBab", lx, y + 12, 6, variabel={"bab": bab}))
    inst.append(instance("TombolRak", 480, 570, 5))

    events = [
        komentar("MENU: pilih wazan. Klik tombol -> simpan nomor bab ke variabel global BabTarget -> pindah ke scene Hutan.\n"
                 "Setiap tombol (TombolBab) dan label (LabelBab) punya variabel instance 'bab' = 1..6.\n"
                 "Tombol RAK BONEKA membuka scene Koleksi."),
        grup("Saat mulai", [
            E([C("SceneJustBegins", "")], [
                A("PlaySound", "", "audio/suara/pilih_wazan.mp3", "", "100", ""),
                A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaKelinci", "Animation", "=", s("biasa")),
            ]),
            komentar("Isi tulisan tiap label dari daftar NamaBab (variabel global). NamaBab[0] = bab 1, dst."),
            untuk_setiap("LabelBab", [], [
                A("TextContainerCapability::TextContainerBehavior::SetValue", "LabelBab", "Text", "=", "NamaBab[LabelBab.bab - 1]"),
                A("TextObject::SetPadding", "LabelBab", "=", "25"),
            ]),
        ]),
        event_muat_koleksi(),
        event_kepala_mengikuti_badan(),
        grup("Klik tombol", [
            E([C("IsCursorOnObject", "TombolBab", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))], [
                A("SetNumberVariable", "BabTarget", "=", "TombolBab.bab"),
                A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""),
                A("Scene", "", s("Hutan"), ""),
            ]),
            E([C("IsCursorOnObject", "TombolRak", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))], [
                A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""),
                A("Scene", "", s("Koleksi"), ""),
            ]),
        ]),
    ]
    return scene("Menu", objects, inst, events, variables=[var_teks("KoleksiJSON", "")])


# ---------------------------------------------------------------------------
# SCENE 2: HUTAN (permainan utama) -- peta diacak setiap kali main
# ---------------------------------------------------------------------------
SEL = 100                     # ukuran 1 sel peta (px)
KOLOM, BARIS = DUNIA_W // SEL, DUNIA_H // SEL   # 20 x 14 sel
MINI = 8                      # ukuran 1 sel di peta mini (px)
MINI_X, MINI_Y = 1104, 112    # pojok kiri-atas isi peta mini di layar (layer UI)


def scene_hutan():
    T_ARAB = FONT_ARAB_TEBAL
    objects = [
        # ---- HUD (layer UI) ----
        teks("TeksSkor", "0 / 5", 40, FONT_LATIN, (255, 255, 255), tebal=True, garis_tepi=(60, 40, 20), tebal_tepi=4),
        teks("TeksLabelWazan", "Wazan yang dicari:", 20, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 40, 20), tebal_tepi=2),
        teks("TeksWazan", "فَعَلَ - يَفْعُلُ", 44, T_ARAB, (255, 255, 255), tebal=True, garis_tepi=(60, 40, 20), tebal_tepi=4),
        teks("TeksFinish", "FINISH", 18, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 40, 20), tebal_tepi=2),
        # ---- Panel soal (layer UI) ----
        sprite("PanelSoal", [("normal", ["assets/panel_soal.png"], True, 0.2)]),
        teks("TeksSoalArab", "نَصَرَ - يَنْصُرُ", 76, T_ARAB, (30, 30, 30), tebal=True),
        teks("TeksArti", "(menolong)", 28, FONT_LATIN, (110, 110, 110)),
        teks("TeksPertanyaan", "Apakah termasuk wazan:", 30, FONT_LATIN, (60, 40, 20)),
        teks("TeksWazanTanya", "فَعَلَ - يَفْعُلُ", 52, T_ARAB, (200, 90, 20), tebal=True),
        sprite("TombolYa", [("normal", ["assets/tombol_ya.png"], True, 0.2)]),
        sprite("TombolTidak", [("normal", ["assets/tombol_tidak.png"], True, 0.2)]),
        # ---- Panel hasil (bawah, supaya petualang & kelinci tetap terlihat) ----
        sprite("PanelHasil", [("normal", ["assets/panel_hasil.png"], True, 0.2)]),
        teks("TeksHasil", "Benar!", 34, FONT_LATIN, (40, 140, 60), tebal=True),
        teks("TeksHasilArab", "فَعَلَ - يَفْعُلُ", 44, T_ARAB, (200, 60, 40), tebal=True),
    ]
    inst = [instance("Rumput", 0, 0, 0, w=DUNIA_W, h=DUNIA_H)]
    # pemain (posisinya nanti dipindah ke sel START saat scene mulai)
    inst.append(instance("Petualang", 118, 118, 10))
    inst.append(instance("KepalaPetualang", 122, 68, 11))
    inst.append(instance("Kelinci", -300, -300, 12))
    inst.append(instance("KepalaKelinci", -300, -362, 13))
    inst.append(instance("TandaStart", 100, 0, 4))
    inst.append(instance("TandaFinish", 1800, 600, 4))
    # HUD
    inst.append(instance("Keranjang", 20, 14, 20, layer="UI"))
    inst.append(instance("TeksSkor", 96, 22, 20, layer="UI"))
    inst.append(instance("TeksLabelWazan", 1050, 2, 20, layer="UI"))
    inst.append(instance("TeksWazan", 1010, 48, 20, layer="UI"))
    inst.append(instance("Panah", 30, 96, 20, layer="UI"))
    inst.append(instance("TeksFinish", 92, 104, 20, layer="UI"))
    # peta mini: panel + titik pemain/start/finish (sel & telur dibuat oleh event saat peta dibuat)
    inst.append(instance("PanelPeta", MINI_X - 8, MINI_Y - 8, 21, layer="UI"))
    inst.append(instance("PetaStart", MINI_X, MINI_Y, 23, layer="UI"))
    inst.append(instance("PetaFinish", MINI_X + 17 * MINI, MINI_Y + 6 * MINI, 23, layer="UI"))
    inst.append(instance("PetaPemain", MINI_X, MINI_Y, 24, layer="UI"))
    # panel soal
    PX, PY = 190, 110
    inst.append(instance("PanelSoal", PX, PY, 30, layer="UI"))
    inst.append(instance("TeksSoalArab", tengah_x("نَصَرَ - يَنْصُرُ", T_ARAB, 76), PY + 28, 31, layer="UI"))
    inst.append(instance("TeksArti", tengah_x("(menolong)", FONT_LATIN, 28), PY + 135, 31, layer="UI"))
    inst.append(instance("TeksPertanyaan", tengah_x("Apakah termasuk wazan:", FONT_LATIN, 30), PY + 178, 31, layer="UI"))
    inst.append(instance("TeksWazanTanya", tengah_x("فَعَلَ - يَفْعُلُ", T_ARAB, 52), PY + 240, 31, layer="UI"))
    inst.append(instance("TombolYa", 395, PY + 335, 31, layer="UI"))
    inst.append(instance("TombolTidak", 665, PY + 335, 31, layer="UI"))
    HY = 520   # panel hasil di bawah layar supaya petualang & kelinci (di tengah) tetap terlihat
    inst.append(instance("PanelHasil", PX, HY, 30, layer="UI"))
    inst.append(instance("TeksHasil", tengah_x("Benar!", FONT_LATIN, 34), HY + 14, 32, layer="UI"))
    inst.append(instance("TeksHasilArab", tengah_x("فَعَلَ - يَفْعُلُ", T_ARAB, 44), HY + 62, 32, layer="UI"))

    variables = [
        var_teks("Status", "jalan"),      # jalan | soal | hasil | salah | tanya_ulang
        var_angka("Skor", 0),
        var_angka("SoalIdx", 0),          # nomor soal yang sedang ditanyakan (indeks di Soal)
        var_teks("Kunci", ""),            # jawaban benar: "ya" / "tidak"
        var_teks("Jawaban", ""),          # jawaban pemain: "ya" / "tidak"
        var_angka("MauYa", 0),            # 1 = cari soal yang jawabannya "ya", 0 = "tidak" (supaya seimbang)
        var_angka("Ketemu", 0),
        var_angka("LamaHasil", 2),        # berapa detik hasil (benar) ditampilkan
        var_angka("TahapSalah", 0),       # urutan adegan saat salah: 0 kaget, 1 jadi telur, 2 kelinci marah, 3 tanya ulang
        var_angka("TelurLayarX", 0),      # posisi telur yang pecah di layar (untuk animasi terbang ke keranjang)
        var_angka("TelurLayarY", 0),
        var_angka("InfoTampil", 0),       # 1 = pesan "telur masih kurang" sedang tampil
        # ---- untuk membuat peta acak ----
        {"name": "Peta", "type": "array", "children": []},   # 20x14 sel: 0 = pohon, 1 = jalur, 2 = jalur+telur
        {"name": "WX", "type": "array", "children": []},     # titik-titik jalur (kolom)
        {"name": "WY", "type": "array", "children": []},     # titik-titik jalur (baris)
        var_angka("Sg", 0), var_angka("X1", 0), var_angka("Y1", 0), var_angka("X2", 0), var_angka("Y2", 0),
        var_angka("K", 0), var_angka("I", 0), var_angka("CX", 0), var_angka("CY", 0),
        var_angka("TelurDibuat", 0),
    ]
    groups = [
        ("GrupSoal", ["PanelSoal", "TeksSoalArab", "TeksArti", "TeksPertanyaan", "TeksWazanTanya", "TombolYa", "TombolTidak"]),
        ("GrupHasil", ["PanelHasil", "TeksHasil", "TeksHasilArab"]),
    ]

    def sel_x(expr):   # posisi x (px) tengah sel dari indeks flat
        return "mod(%s, %d) * %d + %d" % (expr, KOLOM, SEL, SEL // 2)

    def sel_y(expr):
        return "floor(%s / %d) * %d + %d" % (expr, KOLOM, SEL, SEL // 2)

    events = [
        komentar("HUTAN = permainan utama.\n"
                 "Peta dibuat ACAK setiap kali scene dimulai (grup 'Buat peta acak'): jalur dari START (kiri) ke FINISH (kanan)\n"
                 "di grid %dx%d sel (1 sel = %d px), sel di luar jalur diisi Pohon (penghalang).\n"
                 "Alur: Status = \"jalan\" (cari telur) -> \"soal\" (telur pecah, panel soal) -> \"hasil\" (benar) atau\n"
                 "\"salah\" (adegan jadi telur + kelinci) -> ... Sampai FINISH dengan Skor >= TargetTelur -> scene Menang." % (KOLOM, BARIS, SEL)),
        grup("Saat mulai", [
            E([C("SceneJustBegins", "")], [
                A("SetNumberVariable", "Skor", "=", "0"),
                A("SetStringVariable", "Status", "=", s("jalan")),
                A("Hide", "GrupSoal"),
                A("Hide", "GrupHasil"),
                A("Hide", "Kelinci"),
                A("Hide", "KepalaKelinci"),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksSkor", "Text", "=", 'ToString(Skor) + " / " + ToString(TargetTelur)'),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksWazan", "Text", "=", "NamaBab[BabTarget - 1]"),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksWazanTanya", "Text", "=", "NamaBab[BabTarget - 1]"),
                A("SetCenterX", "TeksWazanTanya", "=", str(LEBAR / 2)),
                A("PlaySound", "", "audio/suara/mulai.mp3", "", "100", ""),
                A("ResetTimer", "", s("info")),
            ]),
            komentar("Teks Arab butuh ruang ekstra (padding) supaya harakat di atas huruf tidak terpotong."),
            E([C("SceneJustBegins", "")], [
                A("TextObject::SetPadding", "TeksSoalArab", "=", "40"),
                A("TextObject::SetPadding", "TeksWazanTanya", "=", "30"),
                A("TextObject::SetPadding", "TeksHasilArab", "=", "25"),
                A("TextObject::SetPadding", "TeksWazan", "=", "25"),
            ]),
        ]),
        grup("Buat peta acak (dijalankan sekali saat scene mulai)", [
            komentar("Langkah 1: siapkan grid Peta = %d sel, semua 0 (= pohon)." % (KOLOM * BARIS)),
            E([C("SceneJustBegins", "")], [], [
                ulangi(str(KOLOM * BARIS), [], [A("PushNumber", "Peta", "0")]),
            ]),
            komentar("Langkah 2: pilih 5 titik jalur (WX,WY): START di kolom 1, lalu 3 titik acak makin ke kanan, FINISH di kolom %d.\n"
                     "Barisnya acak (2..%d) -> jalur berkelok naik-turun, beda setiap kali main. (Baris/kolom paling tepi tetap pohon.)" % (KOLOM - 3, BARIS - 3)),
            E([C("SceneJustBegins", "")], [
                A("PushNumber", "WX", "1"), A("PushNumber", "WY", "RandomInRange(2, %d)" % (BARIS - 3)),
                A("PushNumber", "WX", "RandomInRange(5, 8)"), A("PushNumber", "WY", "RandomInRange(2, %d)" % (BARIS - 3)),
                A("PushNumber", "WX", "RandomInRange(9, 12)"), A("PushNumber", "WY", "RandomInRange(2, %d)" % (BARIS - 3)),
                A("PushNumber", "WX", "RandomInRange(13, 16)"), A("PushNumber", "WY", "RandomInRange(2, %d)" % (BARIS - 3)),
                A("PushNumber", "WX", str(KOLOM - 3)), A("PushNumber", "WY", "RandomInRange(2, %d)" % (BARIS - 3)),
                A("SetNumberVariable", "Sg", "=", "0"),
            ]),
            komentar("Langkah 3: sambungkan titik ke titik dengan bentuk huruf L (mendatar dulu, lalu tegak), lebar jalur 3 sel.\n"
                     "Sel jalur diberi nilai 1. Indeks sel = baris * %d + kolom." % KOLOM),
            E([C("SceneJustBegins", "")], [], [
                ulangi("4", [], [
                    A("SetNumberVariable", "X1", "=", "WX[Sg]"), A("SetNumberVariable", "Y1", "=", "WY[Sg]"),
                    A("SetNumberVariable", "X2", "=", "WX[Sg + 1]"), A("SetNumberVariable", "Y2", "=", "WY[Sg + 1]"),
                    A("SetNumberVariable", "K", "=", "0"),
                ], sub=[
                    ulangi("X2 - X1 + 1", [], [                       # mendatar di baris Y1, dari X1 ke X2
                        A("SetNumberVariable", "CX", "=", "X1 + K"),
                        A("SetNumberVariable", "K", "+", "1"),
                        A("SetNumberVariable", "Peta[(Y1 - 1) * %d + CX]" % KOLOM, "=", "1"),
                        A("SetNumberVariable", "Peta[Y1 * %d + CX]" % KOLOM, "=", "1"),
                        A("SetNumberVariable", "Peta[(Y1 + 1) * %d + CX]" % KOLOM, "=", "1"),
                    ]),
                    E([], [A("SetNumberVariable", "K", "=", "0")]),
                    ulangi("abs(Y2 - Y1) + 1", [], [                  # tegak di kolom X2, dari Y1 ke Y2
                        A("SetNumberVariable", "CY", "=", "min(Y1, Y2) + K"),
                        A("SetNumberVariable", "K", "+", "1"),
                        A("SetNumberVariable", "Peta[CY * %d + X2 - 1]" % KOLOM, "=", "1"),
                        A("SetNumberVariable", "Peta[CY * %d + X2]" % KOLOM, "=", "1"),
                        A("SetNumberVariable", "Peta[CY * %d + X2 + 1]" % KOLOM, "=", "1"),
                    ]),
                    E([], [A("SetNumberVariable", "Sg", "+", "1")]),
                ]),
            ]),
            komentar("Langkah 4: tanam Pohon di setiap sel yang masih 0 (sedikit digeser acak supaya alami). Pohon = penghalang."),
            E([C("SceneJustBegins", "")], [A("SetNumberVariable", "I", "=", "0")], [
                ulangi(str(KOLOM * BARIS), [], [
                    # sel peta mini (layer UI): warna gelap untuk pohon, terang untuk jalur
                    A("Create", "", "PetaSel", "%d + mod(I, %d) * %d" % (MINI_X, KOLOM, MINI), "%d + floor(I / %d) * %d" % (MINI_Y, KOLOM, MINI), s("UI")),
                    A("SetZOrder", "PetaSel", "=", "22"),
                    A("AnimatableCapability::AnimatableBehavior::SetName", "PetaSel", "Animation", "=", s("jalur")),
                ], sub=[
                    E([C("NumberVariable", "Peta[I]", "=", "0")], [
                        A("Create", "", "Pohon", sel_x("I") + " - 64 + RandomInRange(-6, 6)", sel_y("I") + " - 80 + RandomInRange(-6, 6)", ""),
                        A("AnimatableCapability::AnimatableBehavior::SetName", "PetaSel", "Animation", "=", s("pohon")),
                    ]),
                    E([], [A("SetNumberVariable", "I", "+", "1")]),
                ]),
            ]),
            komentar("Langkah 5: taruh telur di sel jalur acak (nilai 1 -> jadi 2), tidak terlalu dekat START. Jumlah = JumlahTelurDiHutan.\n"
                     "Dicoba sampai 500 kali supaya jumlahnya pasti cukup."),
            E([C("SceneJustBegins", "")], [A("SetNumberVariable", "TelurDibuat", "=", "0")], [
                ulangi("500", [C("NumberVariable", "TelurDibuat", "<", "JumlahTelurDiHutan")],
                       [A("SetNumberVariable", "I", "=", "RandomInRange(0, %d)" % (KOLOM * BARIS - 1))], sub=[
                    E([C("NumberVariable", "Peta[I]", "=", "1"),
                       C("BuiltinCommonInstructions::CompareNumbers", "abs(mod(I, %d) - WX[0]) + abs(floor(I / %d) - WY[0])" % (KOLOM, KOLOM), ">", "3")], [
                        A("Create", "", "Telur", sel_x("I") + " - 24", sel_y("I") + " - 30", ""),
                        A("SetNumberObjectVariable", "Telur", "sel", "=", "I"),
                        A("Create", "", "PetaTelur", "%d + mod(I, %d) * %d + 1" % (MINI_X, KOLOM, MINI), "%d + floor(I / %d) * %d + 1" % (MINI_Y, KOLOM, MINI), s("UI")),
                        A("SetNumberObjectVariable", "PetaTelur", "sel", "=", "I"),
                        A("SetZOrder", "PetaTelur", "=", "23"),
                        A("SetNumberVariable", "Peta[I]", "=", "2"),
                        A("SetNumberVariable", "TelurDibuat", "+", "1"),
                    ]),
                ]),
            ]),
            komentar("Langkah 6: hiasan (bunga, semak) di sel jalur acak, lalu taruh START, FINISH, dan petualang."),
            E([C("SceneJustBegins", "")], [], [
                ulangi("14", [], [A("SetNumberVariable", "I", "=", "RandomInRange(0, %d)" % (KOLOM * BARIS - 1))], sub=[
                    E([C("NumberVariable", "Peta[I]", "=", "1")], [
                        A("Create", "", "Bunga", sel_x("I") + " - 16 + RandomInRange(-30, 30)", sel_y("I") + " - 16 + RandomInRange(-30, 30)", ""),
                    ]),
                ]),
                E([], [
                    A("SetXY", "TandaStart", "=", "WX[0] * %d + 2" % SEL, "=", "(WY[0] - 1) * %d + 2" % SEL),
                    A("SetXY", "TandaFinish", "=", "WX[4] * %d + 2" % SEL, "=", "WY[4] * %d - 30" % SEL),
                    A("SetXY", "Petualang", "=", "WX[0] * %d + %d - 32" % (SEL, SEL // 2), "=", "WY[0] * %d + %d - 32" % (SEL, SEL // 2)),
                    A("SetXY", "PetaStart", "=", "%d + WX[0] * %d - 2" % (MINI_X, MINI), "=", "%d + WY[0] * %d - 2" % (MINI_Y, MINI)),
                    A("SetXY", "PetaFinish", "=", "%d + WX[4] * %d - 2" % (MINI_X, MINI), "=", "%d + WY[4] * %d - 2" % (MINI_Y, MINI)),
                ]),
            ]),
        ], warna=(180, 220, 180)),
        event_kepala_mengikuti_badan(),
        event_kontrol_wasd(),
        event_animasi_petualang(),
        grup("Kamera, batas hutan, pohon penghalang, panah ke FINISH", [
            E([], [
                A("SetX", "Petualang", "=", "clamp(Petualang.X(), 90, %d)" % (DUNIA_W - 90 - 64)),
                A("SetY", "Petualang", "=", "clamp(Petualang.Y(), 90, %d)" % (DUNIA_H - 90 - 64)),
                A("CenterCameraOnObject", "", "Petualang", "", "", ""),
                A("ClampCamera", "", "0", "0", str(DUNIA_W), str(DUNIA_H), "", ""),
                A("SetAngle", "Panah", "=", "AngleBetweenPositions(Petualang.X(), Petualang.Y(), TandaFinish.X(), TandaFinish.Y())"),
                # titik pemain di peta mini: posisi dunia dibagi ukuran sel, dikali ukuran sel mini
                A("SetXY", "PetaPemain", "=", "%d + Petualang.CenterX() / %d * %d - 5" % (MINI_X, SEL, MINI), "=", "%d + Petualang.CenterY() / %d * %d - 5" % (MINI_Y, SEL, MINI)),
            ]),
            komentar("Pohon adalah penghalang: kalau petualang menabrak pohon, dorong keluar (Separate objects)."),
            E([C("CollisionNP", "Petualang", "Pohon", "", "", "")], [
                A("SeparateFromObjects", "Petualang", "Pohon", ""),
            ]),
        ], warna=(150, 200, 120)),
        grup("Sampai FINISH", [
            komentar("Sampai FINISH dengan telur cukup -> Menang (kelinci jadi boneka). Kalau kurang -> pesan, boleh balik cari telur."),
            E([C("StringVariable", "Status", "=", s("jalan")), C("CollisionNP", "Petualang", "TandaFinish", "", "", ""),
               C("NumberVariable", "Skor", ">=", "TargetTelur")], [
                A("Scene", "", s("Menang"), ""),
            ]),
            E([C("StringVariable", "Status", "=", s("jalan")), C("CollisionNP", "Petualang", "TandaFinish", "", "", ""),
               C("NumberVariable", "Skor", "<", "TargetTelur"), C("BuiltinCommonInstructions::Once")], [
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksHasil", "Text", "=",
                  '"Telur masih kurang " + ToString(TargetTelur - Skor) + "! Kembali cari telur dulu."'),
                A("TextObject::ChangeColor", "TeksHasil", s("200;90;20")),
                A("SetCenterX", "TeksHasil", "=", str(LEBAR / 2)),
                A("Hide", "TeksHasilArab"),
                A("Show", "GrupHasil", ""),
                A("Hide", "TeksHasilArab"),
                A("PlaySoundOnChannel", "", "audio/suara/kurang.mp3", "3", "", "100", ""),
                A("ResetTimer", "", s("info")),
                A("SetNumberVariable", "InfoTampil", "=", "1"),
            ]),
            E([C("NumberVariable", "InfoTampil", "=", "1"), C("StringVariable", "Status", "=", s("jalan")),
               C("CompareTimer", "", s("info"), ">", "3")], [
                A("Hide", "GrupHasil"),
                A("SetNumberVariable", "InfoTampil", "=", "0"),
            ]),
        ], warna=(240, 220, 120)),
        grup("Menemukan telur -> telur pecah -> tampilkan soal", [
            E([C("StringVariable", "Status", "=", s("jalan")),
               C("CollisionNP", "Petualang", "Telur", "", "", "")], [
                A("SetStringVariable", "Status", "=", s("soal")),
                A("SetStringVariable", "Jawaban", "=", s("")),
                A("SetNumberVariable", "InfoTampil", "=", "0"),
                A("Hide", "GrupHasil"),
                A("AnimatableCapability::AnimatableBehavior::SetName", "Telur", "Animation", "=", s("pecah")),
                A("PlaySound", "", "audio/sfx/pecah.wav", "", "100", ""),
                A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaPetualang", "Animation", "=", s("kaget")),
                A("AnimatableCapability::AnimatableBehavior::SetName", "Petualang", "Animation", "=", s("diam")),
                A("TopDownMovementBehavior::IgnoreDefaultControls", "Petualang", "TopDownMovement", "yes"),
                # ---- pilih soal acak (seimbang antara jawaban "ya" dan "tidak") ----
                A("SetNumberVariable", "MauYa", "=", "Random(1)"),
                A("SetNumberVariable", "Ketemu", "=", "0"),
            ], sub=[
                komentar("Ambil soal acak sampai 30 kali percobaan, berhenti (Ketemu=1) kalau cocok:\n"
                         "MauYa=1 -> cari soal yang bab-nya = BabTarget (jawaban Ya)\n"
                         "MauYa=0 -> cari soal yang bab-nya BUKAN BabTarget (jawaban Tidak)"),
                ulangi("30", [C("NumberVariable", "Ketemu", "=", "0")], [
                    A("SetNumberVariable", "SoalIdx", "=", "Random(VariableChildCount(Soal) - 1)"),
                ], sub=[
                    E([C("NumberVariable", "MauYa", "=", "1"), C("NumberVariable", "Soal[SoalIdx].bab", "=", "BabTarget")],
                      [A("SetNumberVariable", "Ketemu", "=", "1")]),
                    E([C("NumberVariable", "MauYa", "=", "0"), C("NumberVariable", "Soal[SoalIdx].bab", "!=", "BabTarget")],
                      [A("SetNumberVariable", "Ketemu", "=", "1")]),
                ]),
                komentar("Tentukan kunci jawaban, lalu tampilkan soal di panel."),
                E([C("NumberVariable", "Soal[SoalIdx].bab", "=", "BabTarget")], [A("SetStringVariable", "Kunci", "=", s("ya"))]),
                E([C("NumberVariable", "Soal[SoalIdx].bab", "!=", "BabTarget")], [A("SetStringVariable", "Kunci", "=", s("tidak"))]),
                E([], [
                    A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksSoalArab", "Text", "=", 'Soal[SoalIdx].madhi + " - " + Soal[SoalIdx].mudhari'),
                    A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksArti", "Text", "=", '"(" + Soal[SoalIdx].arti + ")"'),
                    A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksPertanyaan", "Text", "=", s("Apakah termasuk wazan:")),
                    A("SetCenterX", "TeksPertanyaan", "=", str(LEBAR / 2)),
                    A("SetY", "TombolYa", "=", str(PY + 335)),
                    A("SetY", "TombolTidak", "=", str(PY + 335)),
                    A("Show", "GrupSoal", ""),
                    A("SetCenterX", "TeksSoalArab", "=", str(LEBAR / 2)),
                    A("SetCenterX", "TeksArti", "=", str(LEBAR / 2)),
                ]),
                komentar("(Lanjutan, opsional) Bacakan fi'il-nya dengan suara. Ini memakai JavaScript karena\n"
                         "aksi 'Play a sound' di GDevelop tidak bisa memilih nama file dari variabel.\n"
                         "Nama file diambil dari Soal[SoalIdx].suara. Boleh dihapus kalau tidak diinginkan."),
                js(
                    "const idx = runtimeScene.getVariables().get(\"SoalIdx\").getAsNumber();\n"
                    "const soal = runtimeScene.getGame().getVariables().get(\"Soal\").getChild(idx);\n"
                    "const suara = soal.getChild(\"suara\").getAsString();\n"
                    "if (suara) {\n"
                    "  gdjs.evtTools.sound.playSoundOnChannel(runtimeScene, suara, 2, false, 100, 1);\n"
                    "}\n"
                ),
            ]),
        ], warna=(240, 200, 100)),
        grup("Menjawab: klik YA / TIDAK", [
            E([C("StringVariable", "Status", "=", s("soal")),
               C("IsCursorOnObject", "TombolYa", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))],
              [A("SetStringVariable", "Jawaban", "=", s("ya")), A("PlaySound", "", "audio/sfx/klik.wav", "", "100", "")]),
            E([C("StringVariable", "Status", "=", s("soal")),
               C("IsCursorOnObject", "TombolTidak", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))],
              [A("SetStringVariable", "Jawaban", "=", s("tidak")), A("PlaySound", "", "audio/sfx/klik.wav", "", "100", "")]),
            komentar("Kalau sudah ada jawaban -> cocokkan dengan Kunci. Sembunyikan panel soal, hapus telur yang pecah."),
            E([C("StringVariable", "Status", "=", s("soal")), C("StringVariable", "Jawaban", "!=", s(""))], [
                A("Hide", "GrupSoal"),
                A("ResetTimer", "", s("hasil")),
            ], sub=[
                E([C("AnimatableCapability::AnimatableBehavior::Name", "Telur", "Animation", "=", s("pecah")),
                   C("NumberObjectVariable", "PetaTelur", "sel", "=", "Telur.sel")], [
                    A("SetNumberVariable", "TelurLayarX", "=", 'Telur.X() - CameraX("", 0) + SceneWindowWidth() / 2'),
                    A("SetNumberVariable", "TelurLayarY", "=", 'Telur.Y() - CameraY("", 0) + SceneWindowHeight() / 2'),
                    A("Delete", "PetaTelur", ""),   # titik telur di peta mini ikut hilang
                    A("Delete", "Telur", ""),
                ]),
                komentar("BENAR: skor +1, TelurTerbang (objek khusus, di layer UI) terbang ke keranjang, panel hasil tampil sebentar (Status = \"hasil\")."),
                E([C("StringVariable", "Jawaban", "=", "Kunci")], [
                    A("SetStringVariable", "Status", "=", s("hasil")),
                    A("SetNumberVariable", "Skor", "+", "1"),
                    A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksSkor", "Text", "=", 'ToString(Skor) + " / " + ToString(TargetTelur)'),
                    A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksHasil", "Text", "=", s("Benar! Telur masuk keranjang.")),
                    A("TextObject::ChangeColor", "TeksHasil", s("40;140;60")),
                    A("SetCenterX", "TeksHasil", "=", str(LEBAR / 2)),
                    A("Show", "GrupHasil", ""),
                    A("Hide", "TeksHasilArab"),
                    A("PlaySoundOnChannel", "", "audio/suara/benar.mp3", "3", "", "100", ""),
                    A("SetNumberVariable", "LamaHasil", "=", "2.5"),
                    # efek: telur utuh muncul di layer UI di tempat telur tadi, lalu terbang (tween) ke keranjang
                    A("Create", "", "TelurTerbang", "TelurLayarX", "TelurLayarY", s("UI")),
                    A("SetZOrder", "TelurTerbang", "=", "40"),
                    A("Tween::TweenBehavior::AddObjectPositionTween2", "TelurTerbang", "Tween", s("terbang"),
                      "Keranjang.X() + 8", "Keranjang.Y() + 2", s("easeInQuad"), "0.8", "no"),
                ]),
                komentar("SALAH: mulai adegan bertahap (Status = \"salah\"): kaget -> jadi telur -> kelinci marah -> tanya mulai lagi."),
                E([C("StringVariable", "Jawaban", "!=", "Kunci")], [
                    A("SetStringVariable", "Status", "=", s("salah")),
                    A("SetNumberVariable", "TahapSalah", "=", "0"),
                    A("ResetTimer", "", s("salah")),
                    A("PlaySound", "", "audio/sfx/buzz.wav", "", "100", ""),
                    A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaPetualang", "Animation", "=", s("kaget")),
                ]),
            ]),
            komentar("Efek masuk keranjang: saat telur sampai -> bunyi 'ding', telur hilang, keranjang membesar sebentar lalu kembali."),
            E([C("Tween::HasFinished", "TelurTerbang", "Tween", s("terbang"))], [
                A("PlaySound", "", "audio/sfx/ding.wav", "", "100", ""),
                A("Delete", "TelurTerbang", ""),
                A("Tween::TweenBehavior::AddObjectScaleTween3", "Keranjang", "Tween", s("besar"), "1.35", s("easeOutQuad"), "0.12", "no", "yes"),
            ]),
            E([C("Tween::HasFinished", "Keranjang", "Tween", s("besar"))], [
                A("Tween::RemoveTween", "Keranjang", "Tween", s("besar")),
                A("Tween::TweenBehavior::AddObjectScaleTween3", "Keranjang", "Tween", s("kecil"), "1", s("easeInQuad"), "0.15", "no", "yes"),
            ]),
            E([C("Tween::HasFinished", "Keranjang", "Tween", s("kecil"))], [
                A("Tween::RemoveTween", "Keranjang", "Tween", s("kecil")),
            ]),
        ], warna=(240, 160, 120)),
        grup("Adegan SALAH (bertahap, memakai timer \"salah\" dan variabel TahapSalah)", [
            komentar("Tahap 1 (0,8 detik): POP! petualang berubah jadi telur, kepala disembunyikan, ada efek asap."),
            E([C("StringVariable", "Status", "=", s("salah")), C("NumberVariable", "TahapSalah", "=", "0"),
               C("CompareTimer", "", s("salah"), ">", "0.8")], [
                A("SetNumberVariable", "TahapSalah", "=", "1"),
                A("PlaySound", "", "audio/sfx/pop.wav", "", "100", ""),
                A("AnimatableCapability::AnimatableBehavior::SetName", "Petualang", "Animation", "=", s("telur")),
                A("Hide", "KepalaPetualang"),
                A("Create", "", "Asap", "Petualang.X() - 16", "Petualang.Y() - 30", ""),
            ]),
            komentar("Tahap 2 (1,8 detik): kelinci datang, kepalanya marah, memarahi (suara), tampilkan wazan yang benar."),
            E([C("StringVariable", "Status", "=", s("salah")), C("NumberVariable", "TahapSalah", "=", "1"),
               C("CompareTimer", "", s("salah"), ">", "1.8")], [
                A("SetNumberVariable", "TahapSalah", "=", "2"),
                A("SetX", "Kelinci", "=", "Petualang.X() + 80"),
                A("SetY", "Kelinci", "=", "Petualang.Y() - 8"),
                A("Show", "Kelinci", ""),
                A("Show", "KepalaKelinci", ""),
                A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaKelinci", "Animation", "=", s("marah")),
                A("PlaySoundOnChannel", "", "audio/suara/salah.mp3", "3", "", "100", ""),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksHasil", "Text", "=", s("Salah! Wazan yang benar:")),
                A("TextObject::ChangeColor", "TeksHasil", s("200;60;40")),
                A("SetCenterX", "TeksHasil", "=", str(LEBAR / 2)),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksHasilArab", "Text", "=", "NamaBab[Soal[SoalIdx].bab - 1]"),
                A("SetCenterX", "TeksHasilArab", "=", str(LEBAR / 2)),
                A("Show", "GrupHasil", ""),
            ]),
            komentar("Tahap 3 (6 detik): tanya \"Mau mulai lagi dari awal?\" di panel BAWAH (supaya petualang & kelinci\n"
                     "tidak tertutup), tombol YA/TIDAK dipindah ke panel bawah (Status = \"tanya_ulang\")."),
            E([C("StringVariable", "Status", "=", s("salah")), C("NumberVariable", "TahapSalah", "=", "2"),
               C("CompareTimer", "", s("salah"), ">", "6")], [
                A("SetNumberVariable", "TahapSalah", "=", "3"),
                A("SetStringVariable", "Status", "=", s("tanya_ulang")),
                A("Hide", "TeksHasilArab"),
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksHasil", "Text", "=", s("Mau mulai lagi dari awal?")),
                A("TextObject::ChangeColor", "TeksHasil", s("60;40;20")),
                A("SetCenterX", "TeksHasil", "=", str(LEBAR / 2)),
                A("SetY", "TombolYa", "=", str(HY + 84)),
                A("SetY", "TombolTidak", "=", str(HY + 84)),
                A("Show", "TombolYa", ""),
                A("Show", "TombolTidak", ""),
                A("PlaySoundOnChannel", "", "audio/suara/mulai_lagi.mp3", "3", "", "100", ""),
            ]),
            komentar("Jawaban: YA = ulang scene Hutan dari awal (skor 0), TIDAK = kembali ke Menu."),
            E([C("StringVariable", "Status", "=", s("tanya_ulang")),
               C("IsCursorOnObject", "TombolYa", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))],
              [A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""), A("Scene", "", s("Hutan"), "")]),
            E([C("StringVariable", "Status", "=", s("tanya_ulang")),
               C("IsCursorOnObject", "TombolTidak", "", "", ""),
               C("MouseButtonFromTextReleased", "", s("Left"))],
              [A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""), A("Scene", "", s("Menu"), "")]),
            komentar("Efek asap hilang sendiri setelah animasinya selesai."),
            E([C("AnimatableCapability::AnimatableBehavior::HasAnimationEnded", "Asap", "Animation")], [A("Delete", "Asap", "")]),
        ], warna=(230, 130, 130)),
        grup("Selesai menampilkan hasil BENAR -> lanjut jalan lagi (menang dicek saat sampai FINISH)", [
            E([C("StringVariable", "Status", "=", s("hasil")),
               C("CompareTimer", "", s("hasil"), ">", "LamaHasil")], [
                A("SetStringVariable", "Status", "=", s("jalan")),
                A("SetStringVariable", "Jawaban", "=", s("")),
                A("Hide", "GrupHasil"),
                A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaPetualang", "Animation", "=", s("normal")),
                A("TopDownMovementBehavior::IgnoreDefaultControls", "Petualang", "TopDownMovement", "no"),
            ]),
        ], warna=(150, 220, 150)),
    ]
    return scene("Hutan", objects, inst, events, variables, layers=[layer(""), layer("UI")], groups=groups)


# ---------------------------------------------------------------------------
# SCENE 3: MENANG  (kelinci jadi boneka koleksi)
# ---------------------------------------------------------------------------
def anim_boneka(ekspresi_bab):
    """Nama animasi Boneka untuk bab tertentu: 'b<bab>_t<tingkat>'; tingkat = jumlah menang (maks 4)."""
    return '"b" + ToString(%s) + "_t" + ToString(clamp(Koleksi[%s - 1], 1, 4))' % (ekspresi_bab, ekspresi_bab)


def scene_menang():
    TW = {"name": "Tween", "type": "Tween::TweenBehavior"}
    objects = [
        teks("TeksHebat", "Hebat!", 90, FONT_LATIN, (255, 240, 120), tebal=True, garis_tepi=(90, 60, 30), tebal_tepi=6),
        teks("TeksMenang", "Kamu sampai FINISH dengan telur cukup!", 34, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 90, 40), tebal_tepi=3),
        teks("TeksJumlahBoneka", "Boneka wazan ini: x1", 26, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 90, 40), tebal_tepi=2),
        sprite("TombolLagi", [("normal", ["assets/tombol_lagi.png"], True, 0.2)]),
        sprite("TombolRak", [("normal", ["assets/tombol_rak.png"], True, 0.2)], behaviors=[TW]),
    ]
    inst = [instance("Rumput", 0, 0, 0, w=LEBAR, h=TINGGI)]
    for (x, y) in [(-10, 40), (1150, 20), (-30, 520), (1160, 500)]:
        inst.append(instance("Pohon", x, y, 2))
    inst.append(instance("TeksHebat", tengah_x("Hebat!", FONT_LATIN, 90), 30, 5))
    inst.append(instance("TeksMenang", tengah_x("Kamu sampai FINISH dengan telur cukup!", FONT_LATIN, 34), 160, 5))
    inst.append(instance("TeksJumlahBoneka", tengah_x("Boneka wazan ini: x1", FONT_LATIN, 26), 470, 5))
    inst.append(instance("Keranjang", 470, 380, 5))
    for (x, y) in [(458, 348), (488, 342), (514, 352)]:
        inst.append(instance("Telur", x, y, 4))
    inst.append(instance("Petualang", 360, 350, 10))
    inst.append(instance("KepalaPetualang", 364, 300, 11))
    inst.append(instance("Kelinci", 660, 330, 10))
    inst.append(instance("KepalaKelinci", 656, 268, 11))
    inst.append(instance("Boneka", 640, 240, 12, w=154, h=192))
    inst.append(instance("TombolLagi", 300, 560, 5))
    inst.append(instance("TombolRak", 660, 563, 5))
    events = [
        komentar("MENANG: sampai FINISH dengan telur cukup. Adegan bertahap (timer \"menang\"):\n"
                 "1,2 dtk: POP! kelinci berubah jadi BONEKA (efek asap)  ->  2,4 dtk: boneka terbang masuk ke tombol RAK BONEKA\n"
                 "-> sampai: 'ding', tombol rak membesar sebentar, jumlah boneka ditampilkan.\n"
                 "Koleksi[BabTarget-1] bertambah 1 dan disimpan ke perangkat (Storage). Tingkat boneka: 1 polos, 2 pita, 3 topi, 4+ mahkota."),
        E([C("SceneJustBegins", "")], [
            A("ResetTimer", "", s("menang")),
            A("SetNumberVariable", "Tahap", "=", "0"),
            A("SetNumberVariable", "Koleksi[BabTarget - 1]", "+", "1"),
            A("EcrireFichierTxt", s("TelurWazan"), s("koleksi"), "ToJSON(Koleksi)"),
            A("AnimatableCapability::AnimatableBehavior::SetName", "Boneka", "Animation", "=", anim_boneka("BabTarget")),
            A("Hide", "Boneka"),
            A("Hide", "TeksJumlahBoneka"),
            A("AnimatableCapability::AnimatableBehavior::SetName", "KepalaKelinci", "Animation", "=", s("biasa")),
            A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksJumlahBoneka", "Text", "=",
              '"Boneka wazan ini: x" + ToString(Koleksi[BabTarget - 1]) + "   •   Semua boneka: x" + ToString(Koleksi[0] + Koleksi[1] + Koleksi[2] + Koleksi[3] + Koleksi[4] + Koleksi[5])'),
            A("SetCenterX", "TeksJumlahBoneka", "=", str(LEBAR / 2)),
            A("PlaySound", "", "audio/sfx/menang.wav", "", "100", ""),
        ]),
        event_kepala_mengikuti_badan(),
        grup("Adegan: kelinci jadi boneka, lalu masuk rak", [
            E([C("NumberVariable", "Tahap", "=", "0"), C("CompareTimer", "", s("menang"), ">", "1.2")], [
                A("SetNumberVariable", "Tahap", "=", "1"),
                A("PlaySound", "", "audio/sfx/pop.wav", "", "100", ""),
                A("Create", "", "Asap", "Kelinci.X() - 16", "Kelinci.Y() - 40", ""),
                A("Hide", "Kelinci"),
                A("Hide", "KepalaKelinci"),
                A("Show", "Boneka", ""),
                A("PlaySoundOnChannel", "", "audio/suara/boneka.mp3", "3", "", "100", ""),
            ]),
            E([C("NumberVariable", "Tahap", "=", "1"), C("CompareTimer", "", s("menang"), ">", "2.6")], [
                A("SetNumberVariable", "Tahap", "=", "2"),
                A("Tween::TweenBehavior::AddObjectPositionTween2", "Boneka", "Tween", s("masukRak"),
                  "TombolRak.CenterX() - Boneka.Width() / 2", "TombolRak.CenterY() - Boneka.Height() / 2", s("easeInQuad"), "1", "no"),
                A("Tween::TweenBehavior::AddObjectScaleTween3", "Boneka", "Tween", s("mengecil"), "0.35", s("easeInQuad"), "1", "no", "yes"),
            ]),
            E([C("Tween::HasFinished", "Boneka", "Tween", s("masukRak"))], [
                A("Tween::RemoveTween", "Boneka", "Tween", s("masukRak")),
                A("Hide", "Boneka"),
                A("PlaySound", "", "audio/sfx/ding.wav", "", "100", ""),
                A("Show", "TeksJumlahBoneka", ""),
                A("Tween::TweenBehavior::AddObjectScaleTween3", "TombolRak", "Tween", s("besar"), "1.15", s("easeOutQuad"), "0.12", "no", "yes"),
            ]),
            E([C("Tween::HasFinished", "TombolRak", "Tween", s("besar"))], [
                A("Tween::RemoveTween", "TombolRak", "Tween", s("besar")),
                A("Tween::TweenBehavior::AddObjectScaleTween3", "TombolRak", "Tween", s("kecil"), "1", s("easeInQuad"), "0.15", "no", "yes"),
            ]),
            E([C("Tween::HasFinished", "TombolRak", "Tween", s("kecil"))], [A("Tween::RemoveTween", "TombolRak", "Tween", s("kecil"))]),
            E([C("AnimatableCapability::AnimatableBehavior::HasAnimationEnded", "Asap", "Animation")], [A("Delete", "Asap", "")]),
        ], warna=(230, 200, 240)),
        E([C("IsCursorOnObject", "TombolLagi", "", "", ""), C("MouseButtonFromTextReleased", "", s("Left"))], [
            A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""),
            A("Scene", "", s("Menu"), ""),
        ]),
        E([C("IsCursorOnObject", "TombolRak", "", "", ""), C("MouseButtonFromTextReleased", "", s("Left"))], [
            A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""),
            A("Scene", "", s("Koleksi"), ""),
        ]),
    ]
    return scene("Menang", objects, inst, events, variables=[var_angka("Tahap", 0)])


# ---------------------------------------------------------------------------
# SCENE 4: KOLEKSI (rak boneka)
# ---------------------------------------------------------------------------
def scene_koleksi():
    objects = [
        teks("TeksJudulRak", "Rak Boneka Kelinci", 60, FONT_LATIN, (255, 255, 255), tebal=True, garis_tepi=(90, 60, 30), tebal_tepi=5),
        teks("TeksTotal", "Semua boneka: x0", 26, FONT_LATIN, (255, 255, 255), garis_tepi=(60, 90, 40), tebal_tepi=2),
        teks("LabelWazan", "wazan", 34, FONT_ARAB_TEBAL, (255, 255, 255), tebal=True, garis_tepi=(60, 40, 20), tebal_tepi=3, variables=[var_angka("bab", 1)]),
        teks("TeksJumlah", "x0", 30, FONT_LATIN, (255, 240, 120), tebal=True, garis_tepi=(90, 60, 30), tebal_tepi=3, variables=[var_angka("bab", 1)]),
        sprite("TombolKembali", [("normal", ["assets/tombol_kembali.png"], True, 0.2)]),
    ]
    inst = [instance("Rumput", 0, 0, 0, w=LEBAR, h=TINGGI)]
    inst.append(instance("TeksJudulRak", tengah_x("Rak Boneka Kelinci", FONT_LATIN, 60), 20, 5))
    inst.append(instance("TeksTotal", tengah_x("Semua boneka: x0", FONT_LATIN, 26), 100, 5))
    kolom_x = [190, 590, 990]
    baris_y = [150, 400]
    for i in range(6):
        bab = i + 1
        x, y = kolom_x[i % 3], baris_y[i // 3]
        inst.append(instance("Semak", x - 40, y + 95, 1))
        inst.append(instance("Boneka", x + 2, y, 5, variabel={"bab": bab}))
        inst.append(instance("TeksJumlah", x + 110, y + 40, 6, variabel={"bab": bab}))
        lx = round(x + 50 - lebar_teks(NAMA_BAB[i], FONT_ARAB_TEBAL, 34) / 2)
        inst.append(instance("LabelWazan", lx, y + 128, 6, variabel={"bab": bab}))
    inst.append(instance("TombolKembali", 510, 630, 5))
    events = [
        komentar("KOLEKSI: rak 6 boneka (satu per wazan). Jumlah menang tiap wazan ada di variabel global Koleksi[bab-1]\n"
                 "(dimuat dari penyimpanan). Belum pernah menang -> boneka abu-abu '?'."),
        event_muat_koleksi(),
        grup("Isi rak", [
            untuk_setiap("Boneka", [C("NumberVariable", "Koleksi[Boneka.bab - 1]", "=", "0")], [
                A("AnimatableCapability::AnimatableBehavior::SetName", "Boneka", "Animation", "=", s("kosong")),
            ]),
            untuk_setiap("Boneka", [C("NumberVariable", "Koleksi[Boneka.bab - 1]", ">", "0")], [
                A("AnimatableCapability::AnimatableBehavior::SetName", "Boneka", "Animation", "=", anim_boneka("Boneka.bab")),
            ]),
            untuk_setiap("TeksJumlah", [], [
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksJumlah", "Text", "=", '"x" + ToString(Koleksi[TeksJumlah.bab - 1])'),
            ]),
            untuk_setiap("LabelWazan", [], [
                A("TextContainerCapability::TextContainerBehavior::SetValue", "LabelWazan", "Text", "=", "NamaBab[LabelWazan.bab - 1]"),
                A("TextObject::SetPadding", "LabelWazan", "=", "20"),
            ]),
            E([C("SceneJustBegins", "")], [
                A("TextContainerCapability::TextContainerBehavior::SetValue", "TeksTotal", "Text", "=",
                  '"Semua boneka: x" + ToString(Koleksi[0] + Koleksi[1] + Koleksi[2] + Koleksi[3] + Koleksi[4] + Koleksi[5])'),
                A("SetCenterX", "TeksTotal", "=", str(LEBAR / 2)),
            ]),
        ]),
        E([C("IsCursorOnObject", "TombolKembali", "", "", ""), C("MouseButtonFromTextReleased", "", s("Left"))], [
            A("PlaySound", "", "audio/sfx/klik.wav", "", "100", ""),
            A("Scene", "", s("Menu"), ""),
        ]),
    ]
    return scene("Koleksi", objects, inst, events, variables=[var_teks("KoleksiJSON", "")])


# ---------------------------------------------------------------------------
# PROYEK
# ---------------------------------------------------------------------------
def variabel_global():
    soal = []
    for d in daftar_soal():
        soal.append({"type": "structure", "children": [
            var_teks("madhi", d["madhi"]),
            var_teks("mudhari", d["mudhari"]),
            var_teks("arti", d["arti"]),
            var_angka("bab", d["bab"]),
            var_teks("suara", f"audio/soal/{d['slug']}.mp3"),
        ]})
    return [
        var_angka("TargetTelur", 5),
        var_angka("JumlahTelurDiHutan", 10),   # harus >= TargetTelur (telur tidak muncul lagi setelah diambil)
        var_angka("BabTarget", 1),
        var_array_teks("NamaBab", NAMA_BAB),
        {"name": "Koleksi", "type": "array", "children": [{"type": "number", "value": 0} for _ in range(6)]},  # jumlah boneka per wazan
        {"name": "Soal", "type": "array", "children": soal},
    ]


def proyek():
    objs = objek_global()
    return {
        "firstLayout": "Menu",
        "gdVersion": {"build": 99, "major": 4, "minor": 0, "revision": 0},
        "properties": {
            "adaptGameResolutionAtRuntime": False, "antialiasingMode": "MSAA", "antialisingEnabledOnMobile": False,
            "folderProject": False, "orientation": "landscape", "packageName": "com.keluarga.telurwazan",
            "pixelsRounding": False, "projectUuid": "7e0a1c2e-3b7d-4a3a-9c1e-telurwazan001"[:36],
            "scaleMode": "linear", "sizeOnStartupMode": "adaptWidth", "templateSlug": "",
            "version": "1.0.0", "name": "Telur Wazan",
            "description": "Petualangan mencari telur di hutan sambil belajar wazan (shorof).",
            "author": "", "windowWidth": LEBAR, "windowHeight": TINGGI, "latestCompilationDirectory": "",
            "maxFPS": 60, "minFPS": 20, "verticalSync": False,
            "platformSpecificAssets": {"desktop-icon-512": "assets/ikon.png"},
            "loadingScreen": {"backgroundColor": 7714898, "backgroundFadeInDuration": 0.2, "backgroundImageResourceName": "",
                              "gdevelopLogoStyle": "light", "logoAndProgressFadeInDuration": 0.2,
                              "logoAndProgressLogoFadeInDelay": 0.2, "minDuration": 1.5, "progressBarColor": 16777215,
                              "progressBarHeight": 20, "progressBarMaxWidth": 200, "progressBarMinWidth": 40,
                              "progressBarWidthPercent": 30, "showGDevelopSplash": True, "showProgressBar": True},
            "watermark": {"placement": "bottom-left", "showWatermark": True},
            "authorIds": [], "authorUsernames": [], "categories": ["educational"], "playableDevices": ["keyboard", "mobile"],
            "extensionProperties": [],
            "platforms": [{"name": "GDevelop JS platform"}], "currentPlatform": "GDevelop JS platform",
        },
        "resources": {"resources": kumpulkan_resources(), "resourceFolders": []},
        "objects": objs,
        "objectsFolderStructure": {"folderName": "__ROOT", "children": [{"objectName": o["name"]} for o in objs]},
        "objectsGroups": [],
        "variables": variabel_global(),
        "layouts": [scene_menu(), scene_hutan(), scene_menang(), scene_koleksi()],
        "externalEvents": [],
        "eventsFunctionsExtensions": [],
        "externalLayouts": [],
        "externalSourceFiles": [],
    }


if __name__ == "__main__":
    p = proyek()
    # projectUuid harus UUID yang valid
    p["properties"]["projectUuid"] = "7e0a1c2e-3b7d-4a3a-9c1e-0000c0ffee01"
    tujuan = ROOT / "game.json"
    tujuan.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Ditulis:", tujuan, f"({tujuan.stat().st_size // 1024} KB), soal: {len(daftar_soal())}, resources: {len(p['resources']['resources'])}")
