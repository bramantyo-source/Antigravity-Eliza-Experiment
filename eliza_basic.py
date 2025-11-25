import re
import random

# Pola dan Respon
# Format: (Regex Pattern, [Daftar Respon Alternatif])
PAIRS = [
    [
        r'aku (?:merasa|lagi|sedang) (.*)',
        [
            "Kenapa kamu merasa %1?",
            "Sejak kapan kamu merasa %1?",
            "Ceritakan lebih banyak tentang perasaan %1 itu."
        ]
    ],
    [
        r'(.*) (takut|khawatir|cemas) (.*)',
        [
            "Apa yang membuatmu %2?",
            "Sudahkah kamu mencoba menghadapi rasa %2 itu?"
        ]
    ],
    [
        r'(.*) (ibuku|ayahku|adikku|kakakku|orang tua) (.*)',
        [
            "Ceritakan lebih banyak tentang keluargamu.",
            "Bagaimana hubunganmu dengan mereka?"
        ]
    ],
    [
        r'apakah (.*)',
        [
            "Menurutmu bagaimana?",
            "Mungkin iya, mungkin tidak."
        ]
    ],
    [
        r'kenapa (.*)',
        [
            "Apakah kamu benar-benar tidak tahu alasannya?",
            "Coba tebak kenapa."
        ]
    ],
    [
        r'(.*)\?',
        [
            "Pertanyaan yang menarik.",
            "Kenapa kamu menanyakan itu?"
        ]
    ],
    [
        r'halo|hi|hai|pagi|siang|malam',
        [
            "Halo! Apa yang sedang kamu pikirkan?",
            "Hai. Aku di sini mendengarkan."
        ]
    ],
    [
        r'(.*)',
        [
            "Ceritakan lebih lanjut.",
            "Hmm, menarik. Teruskan.",
            "Aku mendengarkan."
        ]
    ]
]

def analyze(statement):
    """
    Mencocokkan input user dengan pola regex dan mengembalikan respon.
    """
    for pattern, responses in PAIRS:
        match = re.match(pattern, statement.lower())
        if match:
            response = random.choice(responses)
            # Ganti %1, %2, dst dengan grup regex (tanpa refleksi)
            groups = match.groups()
            for i, group in enumerate(groups):
                response = response.replace(f'%{i+1}', group)
            return response
            
    return "Maaf, aku tidak mengerti."

def main():
    print("="*50)
    print("ELIZA (BASIC VERSION)")
    print("Ceritakan masalahmu. Ketik 'keluar' untuk berhenti.")
    print("="*50)

    while True:
        user_input = input("\nAnda: ")
        if user_input.lower() in ['keluar', 'exit', 'bye', 'quit']:
            print("ELIZA: Sampai jumpa.")
            break
        
        if not user_input.strip():
            continue

        print("ELIZA: " + analyze(user_input))

if __name__ == "__main__":
    main()
