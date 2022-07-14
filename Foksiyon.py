def merhaba(isim):
    print("Merhaba " + isim)


merhaba("Yusuf")


def dörtislem(x, y):
    print(f"toplamları {x+y}")
    print(f"farkları {x - y}")
    print(f"çarğımları {x * y}")
    print(f"bölümleri {x / y}")
    print(f"modları {x % y}")


dörtislem(20, 2)

def yasHesapla(dogumYili):
    return 2022 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):   
    yas =yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(2000, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')
























































