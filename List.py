Arabalar = ['Mercedes', 'Bmw', 'Audi', 'Ford']  # List'e eleman ekledik

print(Arabalar[2])  # listteki 2. indeksi yazdırdık

İller = ['İstanbul', 'Hatay', 'Ankara', 'İzmir']  # İller diye bir list oluşturduk

print(İller[0:3])  # İller listimizin 0 ve 2. indeki dahil aradaki elemanları yazdırdık

Uzunluk = len(İller)  # iller list inin uzunluğunu ölçtük
print("Uzunluk : ", (Uzunluk))  # list in uzunluğunu yazdırdık

Sayılar = ['1', '3', '4', '8', '7']  # sayılar diye bir list girdik

İkikatı = [int(2) * int(x) for x in
           Sayılar]  # sayılar listindeki her bir değerin iki katını aldırıp yeni liste haline getiren bir kod yazdık

print(İkikatı)  # ikikatı listesini yazdırdık

enkucuk = min(Sayılar)  # sayılar listesindeki en küçük değeri enkucuk diye bir değişkene atadık
print("En küçük değer :", enkucuk)  # En küçük dğeri yazdırdık

enbuyuk = max(Sayılar)  # Sayılar listesindeki en büyük değeri enbuyuk diye bir değişkene atadık
print("En büyük değer : ", enbuyuk)  # En büyük değeri yazdırdık

y= input("bir sayı giriniz :") #kullanıcıdan y diye bir değişken aldık

if y in Sayılar: #y değişkeninin Sayılar listesinde olup olmadığını sorguladık
    print("aradığınız",y,"sayısı sayılar listesinde bulunmaktadır") #varsa bu çıktıyı vermesini istedik
else:
    print("aradığınız",y,"sayısı sayılar listesinde bulunmamaktadır")#yoksa bu çıktıyı bize vermesini istedik
