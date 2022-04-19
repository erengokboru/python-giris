print("""Islemler: 
	1-Toplama
	2-Cikarma""")

def hesap():

	sec = int(input("Seciniz 1,2:"))

	sayi1 = int(input("Sayi Giriniz :"))
	sayi2 = int(input("Sayi Giriniz :"))

  if sec == 1:
			topla = sayi1 + sayi2
			print("Sonuc : " , topla) 
			hesap()
		
	elif sec == 2:
			cikar = sayi1 - sayi2
			print("Sonuc : " , cikar)
			hesap()
pass
hesap()
 	
