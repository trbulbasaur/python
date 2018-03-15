## **HW3** ##
```python
def rvs(kelime):
    harfler = []
    for i in range(len(kelime)):
        harfler.append(kelime[i])
    for j in range(int(len(harfler) / 2)):
        harfler[j], harfler[len(harfler) - 1 - j] = harfler[len(harfler) - 1 - j], harfler[j]
    return harfler


var = input("kelime veya cümle giriniz:")
print(rvs(var))
```
> Fonksiyon oluşturdum.Harfler adında bir dizi oluşturdum. Diziden sonra girilen kelimenin boyutu (uzunluğu) kadar dönecek bir for döngüsü oluşturdum.Girilen  kelimedeki harfleri oluşturduğum diziye ekledim. Daha sonra ikinci bir for döngüsü oluşturdum. Bu döngü dizinin uzunluğunun yarısı kadar dönecek. Kelimenin harflerini tersine çevirdim.Çevirme işlemini yaparken ortanca harfin sağındaki harf ile solundaki harfin yerlerini değiştirdim.Döngü yardımıyla bu işlemi diğer harflere de uyguladım. Daha sonra girilen kelimenin tersini ekrana yazdırdım.Sondaki kod ile kullanıcının veri girmesini sağladım.
