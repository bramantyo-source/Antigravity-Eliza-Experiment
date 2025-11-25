import sys
import os

def chat():
    print("="*50)
    print("SmartEliza v1.0 (VULNERABLE VERSION)")
    print("Fitur baru: Ketik 'hitung: <ekspresi>' untuk kalkulator.")
    print("Ketik 'keluar' untuk berhenti.")
    print("="*50)
    
    while True:
        try:
            user_input = input("\nAnda: ")
            if user_input.lower() in ['keluar', 'exit']:
                print("SmartEliza: Bye!")
                break
                
            if user_input.lower().startswith('hitung:'):
                expression = user_input.split(':', 1)[1]
                print(f"SmartEliza: Sedang menghitung '{expression.strip()}'...")
                
                # --- VULNERABILITY START ---
                # Menggunakan eval() pada input user tanpa sanitasi
                # Ini memungkinkan eksekusi kode Python sembarang (RCE)
                result = eval(expression)
                # --- VULNERABILITY END ---
                
                print(f"SmartEliza: Hasilnya adalah {result}")
            else:
                print("SmartEliza: Maaf, saya sedang mode kalkulator. Coba 'hitung: 10 * 5'")
        except Exception as e:
            print(f"SmartEliza: Error - {e}")
        except KeyboardInterrupt:
            print("\nSmartEliza: Force close.")
            break

if __name__ == "__main__":
    chat()
