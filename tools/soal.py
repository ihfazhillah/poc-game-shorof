# -*- coding: utf-8 -*-
"""
Daftar soal (contoh fi'il tsulatsi mujarrad) untuk game Telur Wazan.

Dipakai oleh:
  - tools/buat_game.py   -> dimasukkan ke variabel global `Soal` di game.json
  - tools/buat_audio.py  -> dibuatkan suara bacaan Arab (audio/soal/<slug>.mp3)

CATATAN: Setelah proyek dibuka di GDevelop, daftar soal juga bisa diubah langsung
di GDevelop (Project manager -> Global variables -> Soal). File ini hanya
sumber awal.

bab: nomor bab tsulatsi mujarrad
  1 = فَعَلَ - يَفْعُلُ   (nashara - yanshuru)
  2 = فَعَلَ - يَفْعِلُ   (dharaba - yadhribu)
  3 = فَعَلَ - يَفْعَلُ   (fataha - yaftahu)
  4 = فَعِلَ - يَفْعَلُ   ('alima - ya'lamu)
  5 = فَعُلَ - يَفْعُلُ   (hasuna - yahsunu)
  6 = فَعِلَ - يَفْعِلُ   (hasiba - yahsibu)
"""

NAMA_BAB = [
    "فَعَلَ - يَفْعُلُ",
    "فَعَلَ - يَفْعِلُ",
    "فَعَلَ - يَفْعَلُ",
    "فَعِلَ - يَفْعَلُ",
    "فَعُلَ - يَفْعُلُ",
    "فَعِلَ - يَفْعِلُ",
]

# Nama bab dalam huruf latin (untuk teks bantu / suara)
NAMA_BAB_LATIN = [
    "fa'ala - yaf'ulu",
    "fa'ala - yaf'ilu",
    "fa'ala - yaf'alu",
    "fa'ila - yaf'alu",
    "fa'ula - yaf'ulu",
    "fa'ila - yaf'ilu",
]

# (slug, madhi, mudhari, arti, bab)
SOAL = [
    # ---- bab 1: فَعَلَ - يَفْعُلُ ----
    ("nashara",  "نَصَرَ", "يَنْصُرُ", "menolong", 1),
    ("kataba",   "كَتَبَ", "يَكْتُبُ", "menulis", 1),
    ("dakhala",  "دَخَلَ", "يَدْخُلُ", "masuk", 1),
    ("kharaja",  "خَرَجَ", "يَخْرُجُ", "keluar", 1),
    ("sajada",   "سَجَدَ", "يَسْجُدُ", "bersujud", 1),
    ("thalaba",  "طَلَبَ", "يَطْلُبُ", "mencari / meminta", 1),
    ("syakara",  "شَكَرَ", "يَشْكُرُ", "bersyukur", 1),
    ("dzakara",  "ذَكَرَ", "يَذْكُرُ", "mengingat / menyebut", 1),
    ("nazhara",  "نَظَرَ", "يَنْظُرُ", "melihat", 1),
    ("qaada",   "قَعَدَ", "يَقْعُدُ", "duduk", 1),
    ("akhadza",  "أَخَذَ", "يَأْخُذُ", "mengambil", 1),
    ("akala",    "أَكَلَ", "يَأْكُلُ", "makan", 1),
    ("razaqa",   "رَزَقَ", "يَرْزُقُ", "memberi rezeki", 1),
    ("sakata",   "سَكَتَ", "يَسْكُتُ", "diam", 1),
    # ---- bab 2: فَعَلَ - يَفْعِلُ ----
    ("dharaba",  "ضَرَبَ", "يَضْرِبُ", "memukul", 2),
    ("jalasa",   "جَلَسَ", "يَجْلِسُ", "duduk", 2),
    ("ghafara",  "غَفَرَ", "يَغْفِرُ", "mengampuni", 2),
    ("hamala",   "حَمَلَ", "يَحْمِلُ", "membawa", 2),
    ("arafa",    "عَرَفَ", "يَعْرِفُ", "mengetahui / mengenal", 2),
    ("ghasala",  "غَسَلَ", "يَغْسِلُ", "mencuci", 2),
    ("kasara",   "كَسَرَ", "يَكْسِرُ", "memecahkan", 2),
    ("shabara",  "صَبَرَ", "يَصْبِرُ", "bersabar", 2),
    ("rajaa",   "رَجَعَ", "يَرْجِعُ", "kembali / pulang", 2),
    ("nazala",   "نَزَلَ", "يَنْزِلُ", "turun", 2),
    ("malaka",   "مَلَكَ", "يَمْلِكُ", "memiliki", 2),
    ("qasama",   "قَسَمَ", "يَقْسِمُ", "membagi", 2),
    ("habasa",   "حَبَسَ", "يَحْبِسُ", "menahan", 2),
    ("zhalama",  "ظَلَمَ", "يَظْلِمُ", "menzalimi", 2),
    # ---- bab 3: فَعَلَ - يَفْعَلُ ----
    ("fataha",   "فَتَحَ", "يَفْتَحُ", "membuka", 3),
    ("dzahaba",  "ذَهَبَ", "يَذْهَبُ", "pergi", 3),
    ("saala",   "سَأَلَ", "يَسْأَلُ", "bertanya", 3),
    ("manaa",   "مَنَعَ", "يَمْنَعُ", "mencegah / melarang", 3),
    ("qaraa",   "قَرَأَ", "يَقْرَأُ", "membaca", 3),
    ("jaala",   "جَعَلَ", "يَجْعَلُ", "menjadikan", 3),
    ("shanaa",  "صَنَعَ", "يَصْنَعُ", "membuat", 3),
    ("rafaa",   "رَفَعَ", "يَرْفَعُ", "mengangkat", 3),
    ("nafaa",   "نَفَعَ", "يَنْفَعُ", "bermanfaat", 3),
    ("zaraa",   "زَرَعَ", "يَزْرَعُ", "menanam", 3),
    ("badaa",   "بَدَأَ", "يَبْدَأُ", "memulai", 3),
    ("dafaa",   "دَفَعَ", "يَدْفَعُ", "mendorong / membayar", 3),
    ("qathaa",  "قَطَعَ", "يَقْطَعُ", "memotong", 3),
    ("syaraha",  "شَرَحَ", "يَشْرَحُ", "menjelaskan", 3),
    # ---- bab 4: فَعِلَ - يَفْعَلُ ----
    ("alima",    "عَلِمَ", "يَعْلَمُ", "mengetahui", 4),
    ("syariba",  "شَرِبَ", "يَشْرَبُ", "minum", 4),
    ("samia",   "سَمِعَ", "يَسْمَعُ", "mendengar", 4),
    ("fahima",   "فَهِمَ", "يَفْهَمُ", "memahami", 4),
    ("hafizha",  "حَفِظَ", "يَحْفَظُ", "menghafal / menjaga", 4),
    ("labisa",   "لَبِسَ", "يَلْبَسُ", "memakai (pakaian)", 4),
    ("fariha",   "فَرِحَ", "يَفْرَحُ", "gembira", 4),
    ("rakiba",   "رَكِبَ", "يَرْكَبُ", "menaiki / mengendarai", 4),
    ("syahida",  "شَهِدَ", "يَشْهَدُ", "menyaksikan", 4),
    ("hazina",   "حَزِنَ", "يَحْزَنُ", "bersedih", 4),
    ("ghadhiba", "غَضِبَ", "يَغْضَبُ", "marah", 4),
    ("dhahika",  "ضَحِكَ", "يَضْحَكُ", "tertawa", 4),
    ("amila",    "عَمِلَ", "يَعْمَلُ", "bekerja / berbuat", 4),
    ("laiba",   "لَعِبَ", "يَلْعَبُ", "bermain", 4),
    ("rahima",   "رَحِمَ", "يَرْحَمُ", "menyayangi", 4),
    ("taiba",   "تَعِبَ", "يَتْعَبُ", "lelah", 4),
    ("hamida",   "حَمِدَ", "يَحْمَدُ", "memuji", 4),
    # ---- bab 5: فَعُلَ - يَفْعُلُ ----
    ("hasuna",   "حَسُنَ", "يَحْسُنُ", "menjadi baik", 5),
    ("kabura",   "كَبُرَ", "يَكْبُرُ", "menjadi besar", 5),
    ("karuma",   "كَرُمَ", "يَكْرُمُ", "menjadi mulia", 5),
    ("bauda",   "بَعُدَ", "يَبْعُدُ", "menjadi jauh", 5),
    ("qaruba",   "قَرُبَ", "يَقْرُبُ", "menjadi dekat", 5),
    ("shauba",  "صَعُبَ", "يَصْعُبُ", "menjadi sulit", 5),
    ("sahula",   "سَهُلَ", "يَسْهُلُ", "menjadi mudah", 5),
    ("shaghura", "صَغُرَ", "يَصْغُرُ", "menjadi kecil", 5),
    ("syarufa",  "شَرُفَ", "يَشْرُفُ", "menjadi mulia / terhormat", 5),
    ("azhuma",   "عَظُمَ", "يَعْظُمُ", "menjadi agung", 5),
    ("katsura",  "كَثُرَ", "يَكْثُرُ", "menjadi banyak", 5),
    ("jamula",   "جَمُلَ", "يَجْمُلُ", "menjadi indah", 5),
    ("lathufa",  "لَطُفَ", "يَلْطُفُ", "menjadi lembut", 5),
    ("tsaqula",  "ثَقُلَ", "يَثْقُلُ", "menjadi berat", 5),
    # ---- bab 6: فَعِلَ - يَفْعِلُ ----
    ("hasiba",   "حَسِبَ", "يَحْسِبُ", "mengira / menyangka", 6),
    ("naima",   "نَعِمَ", "يَنْعِمُ", "hidup senang / nikmat", 6),
    ("waritsa",  "وَرِثَ", "يَرِثُ", "mewarisi", 6),
    ("watsiqa",  "وَثِقَ", "يَثِقُ", "percaya", 6),
    ("yaisa",   "يَئِسَ", "يَيْئِسُ", "putus asa", 6),
    ("wamiqa",   "وَمِقَ", "يَمِقُ", "mencintai", 6),
    ("warima",   "وَرِمَ", "يَرِمُ", "membengkak", 6),
    ("wafiqa",   "وَفِقَ", "يَفِقُ", "cocok / sesuai", 6),
]


def daftar_soal():
    """Kembalikan daftar dict soal."""
    return [dict(slug=s, madhi=m, mudhari=d, arti=a, bab=b) for (s, m, d, a, b) in SOAL]


if __name__ == "__main__":
    from collections import Counter
    c = Counter(b for *_, b in SOAL)
    print("Jumlah soal:", len(SOAL), "per bab:", dict(sorted(c.items())))
    slugs = [s for s, *_ in SOAL]
    assert len(slugs) == len(set(slugs)), "slug ganda!"
