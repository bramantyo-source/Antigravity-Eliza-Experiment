import re
import random

# Refleksi kata ganti: Mengubah sudut pandang pembicara
# Contoh: "Aku benci kamu" -> "Kenapa kamu benci aku?"
REFLECTIONS = {
    "aku": "kamu",
    "saya": "kamu",
    "gue": "kamu",
    "kamu": "aku",
    "anda": "aku",
    "lu": "aku",
    "milikku": "milikmu",
    "punyaku": "punyamu",
    "milikmu": "milikku",
    "punyamu": "punyaku",
    "kita": "kalian",
}

# Pola dan Respon
# Format: (Regex Pattern, [Daftar Respon Alternatif])
# %1, %2, dst akan digantikan oleh grup yang ditangkap regex
PAIRS = [
    [
        r'aku (?:merasa|lagi|sedang) (.*)',
        [
            "Kenapa kamu merasa %1?",
            "Sejak kapan rasa %1 ini muncul?",
            "Apakah rasa %1 ini mengganggu aktivitasmu?",
            "Ceritakan lebih banyak tentang perasaan %1 itu."
        ]
    ],
    [
        r'(.*) (takut|khawatir|cemas) (.*)',
        [
            "Ketakutan seringkali hanya ada di pikiran. Apa bukti nyata dari %3?",
            "Apa hal terburuk yang bisa terjadi jika %3 benar-benar terjadi?",
            "Sudahkah kamu mencoba menghadapi rasa %2 itu?"
        ]
    ],
    [
        r'(.*) (ibuku|ayahku|adikku|kakakku|orang tua) (.*)',
        [
            "Ceritakan lebih banyak tentang keluargamu.",
            "Bagaimana hubunganmu dengan mereka biasanya?",
            "Apakah ini memengaruhi perasaanmu saat ini?",
            "Keluarga memang topik yang emosional. Lanjutkan."
        ]
    ],
    [
        r'(.*) (benci|marah|kesal) (.*)',
        [
            "Mengapa kamu merasa %2 pada %3?",
            "Apakah %3 juga merasakan hal yang sama?",
            "Melepaskan rasa %2 bisa membuatmu lebih lega."
        ]
    ],
    [
        r'(.*) (suka|cinta|sayang) (.*)',
        [
            "Wah, %2 adalah perasaan yang kuat. Ceritakan tentang %3.",
            "Apa yang membuatmu %2 pada %3?",
            "Bagaimana perasaan itu memengaruhi hari-harimu?"
        ]
    ],
    [
        r'apakah (.*)',
        [
            "Menurutmu bagaimana?",
            "Apakah penting bagimu untuk mengetahui jawabannya?",
            "Mungkin iya, mungkin tidak. Apa intuisimu berkata?"
        ]
    ],
    [
        r'kenapa (.*)',
        [
            "Apakah kamu benar-benar tidak tahu alasannya?",
            "Mungkin jawabannya ada di dalam dirimu sendiri.",
            "Coba tebak kenapa."
        ]
    ],
    [
        r'(.*) (mau|ingin|butuh) (.*)',
        [
            "Apa yang akan kamu lakukan jika mendapatkan %3?",
            "Mengapa kamu menginginkan %3?",
            "Apakah %3 benar-benar kebutuhan utamamu saat ini?"
        ]
    ],
    [
        r'(.*)\?',
        [
            "Pertanyaan yang menarik.",
            "Jujur, aku tidak punya jawaban pasti. Bagaimana menurutmu?",
            "Kenapa kamu menanyakan itu?"
        ]
    ],
    [
        r'halo|hi|hai|pagi|siang|malam',
        [
            "Halo! Apa yang sedang kamu pikirkan?",
            "Hai. Aku di sini mendengarkan.",
            "Senang bertemu denganmu. Ada yang mengganjal di hati?"
        ]
    ],
    [
        r'(.*)',
        [
            "Ceritakan lebih lanjut.",
            "Hmm, menarik. Teruskan.",
            "Aku mendengarkan.",
            "Bisa jelaskan lebih detail?",
            "Lalu bagaimana perasaanmu tentang itu?"
        ]
    ]
]

def reflect(fragment):
    """
    Mengubah kata ganti dalam teks sesuai dictionary REFLECTIONS.
    """
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in REFLECTIONS:
            tokens[i] = REFLECTIONS[token]
    return ' '.join(tokens)

def sanitize_input(text):
    """
    Membersihkan input dari karakter berbahaya dan membatasi panjang.
    """
    # 1. Batasi panjang input (Defense against DoS/Buffer Overflow simulation)
    MAX_LENGTH = 200
    if len(text) > MAX_LENGTH:
        print(f"[SYSTEM WARNING] Input terlalu panjang ({len(text)} chars). Dipotong ke {MAX_LENGTH} chars.")
        text = text[:MAX_LENGTH]
    
    # 2. Hapus karakter non-printable (Defense against Control Character Injection)
    # Hanya izinkan huruf, angka, spasi, dan tanda baca dasar
    text = re.sub(r'[^a-zA-Z0-9\s.,?!]', '', text)
    
    return text.strip()

def analyze(statement):
    """
    Mencocokkan input user dengan pola regex dan mengembalikan respon.
    """
    # Terapkan sanitasi sebelum diproses regex
    statement = sanitize_input(statement)
    
    for pattern, responses in PAIRS:
        try:
            # Gunakan timeout atau limit jika memungkinkan (Python re tidak punya timeout bawaan)
            # Tapi dengan limit input 200 chars, ReDoS sangat sulit terjadi.
            match = re.match(pattern, statement.lower())
            if match:
                response = random.choice(responses)
                # Ganti %1, %2, dst dengan grup regex yang direfleksikan
                groups = match.groups()
                for i, group in enumerate(groups):
                    # Refleksikan kata ganti dalam grup yang ditangkap
                    reflected_group = reflect(group)
                    response = response.replace(f'%{i+1}', reflected_group)
                return response
        except re.error:
            # Defense against Regex Errors
            continue
            
    return "Maaf, aku tidak mengerti. Bisa ulangi?"

def main():
    print("="*50)
    print("ELIZA PRO: PSIKOTERAPIS VIRTUAL")
    print("Ceritakan masalahmu. Ketik 'keluar' untuk berhenti.")
    print("="*50)

    while True:
        try:
            user_input = input("\nAnda: ")
            if user_input.lower() in ['keluar', 'exit', 'bye', 'quit']:
                print("\nELIZA: Sampai jumpa. Tetap semangat.")
                break
            
            if not user_input.strip():
                continue

            print("ELIZA: " + analyze(user_input))
            
        except EOFError:
            break

if __name__ == "__main__":
    main()
