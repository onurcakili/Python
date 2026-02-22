def guvenli_bol(a, b):
    try:
        sonuc = a / b
        print(f"Sonuç: {sonuc}")
        
    except ZeroDivisionError:
        print("Sıfıra bölünemez!")
        
    except TypeError:
        print("Sayı giriniz!")
        
    finally:
        print("İşlem tamamlandı.")

guvenli_bol(10, 2)    
guvenli_bol(10, 0)    
guvenli_bol(10, "a")  