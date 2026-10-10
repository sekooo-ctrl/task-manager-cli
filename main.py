import json
import os

DOSYA="gorevler.json"

def gorevleri_yukle():
    if not os.path.exists(DOSYA):
        return []
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

def gorevleri_kaydet(gorevler):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(gorevler, f, ensure_ascii=False, indent=2)

def gorev_ekle(gorevler, baslik):
    gorevler.append({"baslik": baslik, "tamamlandi": False})
    gorevleri_kaydet(gorevler)
    print(f"Görev '{baslik}' eklendi.")

def gorevleri_listele(gorevler):
    if not gorevler:
        print("Görev listesi boş.")
        return
    for i, gorev in enumerate(gorevler, start=1):
        isaret="[x]" if gorev["tamamlandi"] else "[ ]"
        print(f"{i}. {isaret} {gorev['baslik']}")  

def gorev_sil(gorevler, numara):
    if numara < 1 or numara > len(gorevler):
        print("Geçersiz numara.")
        return
    silinen = gorevler.pop(numara - 1)
    gorevleri_kaydet(gorevler)
    print(f"✗ Silindi: {silinen['baslik']}")


def gorev_tamamla(gorevler, numara):
    if numara < 1 or numara > len(gorevler):
        print("Geçersiz numara.")
        return
    gorevler[numara - 1]["tamamlandi"] = True
    gorevleri_kaydet(gorevler)
    print(f"✓ Tamamlandı: {gorevler[numara - 1]['baslik']}")
def sayi_al():
    try:    
        return int(input("Numara: "))
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
        return None

def menu():
    gorevler = gorevleri_yukle()
    while True:
        print("\n--- GÖREV YÖNETİCİSİ ---")
        print("1) Listele  2) Ekle  3) Tamamla  4) Sil  5) Çıkış")
        secim = input("Seçimin: ")

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            baslik = input("Görev: ")
            gorev_ekle(gorevler, baslik)
        elif secim == "3":
            gorevleri_listele(gorevler)
            numara = sayi_al()
            if numara is not None:
                gorev_tamamla(gorevler, numara)
        elif secim == "4":
            gorevleri_listele(gorevler)
            numara = sayi_al()
            if numara is not None:
                gorev_sil(gorevler, numara)
        elif secim == "5":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    menu()