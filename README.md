# Eliza Bot Experiment: Built & Tested with Google Antigravity 🛡️🤖

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Security](https://img.shields.io/badge/Security-Educational-red)

Project ini adalah dokumentasi eksperimen menggunakan **Agentic AI (Google Antigravity)** untuk mensimulasikan siklus *Secure Software Development Life Cycle (SDLC)* secara otomatis.

## 📂 Struktur File
- `vulnerable_bot.py`: Versi bot yang memiliki celah keamanan RCE (Remote Code Execution).
- `exploit_eliza.py`: Script testing/serangan otomatis untuk membuktikan kerentanan.
- `eliza_advanced.py`: Versi bot yang sudah diamankan (Secure) menggunakan Input Sanitization & Regex.

## 🚀 Cara Menjalankan (How to Run)

### 1. Simulasi Serangan (Red Team)
Jalankan script exploit untuk melihat bagaimana serangan DoS/Stress Test bekerja:
```bash
python exploit_eliza.py
```

### 2. Menjalankan Bot Aman (Blue Team)
Coba chat dengan bot yang sudah diamankan:
```
python eliza_advanced.py
```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 📝 Skenario Eksperimen
Vulnerability: Bot awal menggunakan fungsi eval() yang tidak aman.

Exploitation: AI membuat script untuk mengirim 1 juta karakter (DoS) dan injeksi kode.

Hardening: AI memperbaiki kode dengan membatasi panjang input (max 200 chars) dan whitelist karakter menggunakan Regex.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ⚠️ Disclaimer
Repo ini dibuat untuk tujuan EDUKASI dan demonstrasi kemampuan AI Agent dalam Cybersecurity Awareness. Jangan gunakan script exploit untuk target ilegal.



