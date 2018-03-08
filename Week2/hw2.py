kelime = input("Bir kelime giriniz: ")
a = int(input("Baslangic sayisini giriniz: "))
b = int(input("Sonlandirma sayisini giriniz(Kelimedeki harf sayısından büyük olmamalıdır.): "))
if a > len(kelime) or b > len(kelime):
    print("Kelimeden Büyük Değer Girilemez")
else:
    if a == 0 or b ==0:
        print("Sıfır Giremezsiniz")
    else:
        a = a-1
        print(kelime)
        print("{}".format(kelime[:a]+kelime[b:]))