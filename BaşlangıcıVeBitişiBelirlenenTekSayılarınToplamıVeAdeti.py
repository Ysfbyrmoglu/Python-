toplam=0
sayac=0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range (int(baslangic), int(bitis)+1):
   if (int(sayi%2==1)):
        toplam=toplam+sayi
        sayac=sayac+1
print('Aradaki Sayıların Toplamı:',toplam) 
print('Arsadaki Sayıların Toplamı :',sayac) 