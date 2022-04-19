### Eren | Dersler

# İf/Else/Elif Nedir?

# Örnek:

    yas = int(input(":"))
    giris_izni = 18
    izinsiz = 60

    if yas < giris_izni:
	      print("Yasiniz Kucuk")

    elif yas > izinsiz:
	          print("Yasiniz cok Buyuk be!")

    else:
       print("Giris izni Verildi")
       
    
    
# Açıklamalar:      
İf: eğer demektir yukardaki örnekte verdiğim gibi kullanıla bilir.


elif: ise bir if içinde başka bir if gibidir. bir if'in içinde başka bir if yazılmaz bu durumlarda ise karşımıza elif çıkar.


else: aksi taktirde demektir.


# Örnek Hesap Makinesi:

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
 	
       
       
       
