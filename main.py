gorevler=[]
def gorev_ekle(baslik):
    gorevler.append(baslik)
    print(f"Görev '{baslik}' eklendi.")

def gorevleri_listele():
    if not gorevler:
        print("Görev listesi boş.")
    else:
        print("Görevler:")
        for i, gorev in enumerate(gorevler, start=1):
            print(f"{i}. {gorev}")
gorev_ekle("Python çalış")
gorev_ekle("GitHub düzenlemesi")
gorevleri_listele()