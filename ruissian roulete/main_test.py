import random
import os
import sys

def rus_ruleti():
    print("Rus Ruleti başlıyor...")
    hazne = [0, 0, 0, 0, 0, 1]  # 6 hazneli silah, 1 kurşun
    random.shuffle(hazne)       # Hazneyi karıştırıyoruz
    sonuc = random.choice(hazne)

    if sonuc == 1:
        print("Kurşun! Bilgisayar kapanıyor...")
        if sys.platform == "win32":
            os.system("shutdown /s /t 1")  # Windows için
        elif sys.platform == "linux" or sys.platform == "darwin":
            os.system("shutdown now")     # Linux ve macOS için
        else:
            print("Bu platform desteklenmiyor.")
    else:
        print("Şanslısın! Hayatta kaldın.")

if __name__ == "__main__":
    rus_ruleti()
