import random

sayi = random.randrange(1,10)
tahmin_sayisi = 0

while True:
    
    tahmin = int(input("Bir sayi tahmin ediniz : "))
    tahmin_sayisi += 1
    
    if tahmin == sayi:
        print("Doğru!")
        print(f"Tahmin Sayisi: {tahmin_sayisi}")
        break
    elif tahmin > sayi:
        print("Daha küçük bir sayi olmalı!")
    else:
        print("Daha büyük bir sayi olmalı!")


        