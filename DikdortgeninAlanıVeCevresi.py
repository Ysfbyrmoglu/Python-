
kenar1=input('İlk Kenarın Uzunluğunu Girin : ')
kenar2=input('İkinci Kenarın Uzunluğunu Girin: ')
alan=int(kenar1)*int(kenar2)
cevre=2*(int(kenar1)+int(kenar2))
print("Dikdörtgenin Alanı : {0}".format(alan))
print("Dikdörtgenin Çevresi : {0}".format(cevre))

if (kenar1==kenar2):
	print("Dikdörtgenin cinsi karedir" )
