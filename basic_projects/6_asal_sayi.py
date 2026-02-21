sayi = int(input("Bir sayı giriniz: "))

if sayi < 2:
    print("Asal sayı değildir.")
else:
    asal = True
    
    for x in range(2, sayi):
        if sayi % x == 0:
            asal = False
            break
        
    if asal:
        print("Asal sayıdır.")
    else:
        print("Asal sayı değildir.")