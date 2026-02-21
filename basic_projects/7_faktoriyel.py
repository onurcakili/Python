sayi = int(input("Bir sayı giriniz: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i
    
print("{}! = {}".format(sayi, faktoriyel))

