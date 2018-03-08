import random
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
arr[0] = random.randint(1, 99)
random.shuffle(arr)
print(arr)
toplam = 0
for i in arr :
    toplam = toplam + i
sayi = toplam - 4950
print ("Random Sayı:",sayi)
