"""
TCMB Doviz Kuru Cekici

TCMB'nin XML API'sinden doviz kurlarini ceken basit script.
Belirtilen tarih araligindaki EUR, GBP, USD kurlarini TRY bazinda getirir.

Kullanim:
    python fx_rates.py

Cikti:
    fx_rates.xlsx dosyasi (Date, Currency, Rate kolonlari)
"""

import requests
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


def get_fx_rates(start_date, end_date):
    """
    Belirtilen tarih araligindaki doviz kurlarini TCMB API'sinden ceker.
    
    Args:
        start_date (str): Baslangic tarihi (YYYY-MM-DD formatinda)
        end_date (str): Bitis tarihi (YYYY-MM-DD formatinda)
    
    Returns:
        pandas.DataFrame: Date, Currency ve Rate kolonlarini iceren DataFrame
    
    API Yapisi:
        TCMB her gun icin ayri bir XML dosyasi yayinlar.
        URL formati: https://www.tcmb.gov.tr/kurlar/YYYYMM/DDMMYYYY.xml
        
        XML yapisinda her doviz icin:
        - CurrencyCode: Para birimi kodu (EUR, USD, vb)
        - ForexSelling: Doviz satis kuru (TRY bazinda)
    """
    
    # Tum veriler bu listede toplanacak
    all_data = []
    
    # Tarih objelerine donusturuldu
    current = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    # Baslangictan bitise kadar her gun islendi
    while current <= end:
        
        # TCMB URL formati olusturuldu
        # Ornek: https://www.tcmb.gov.tr/kurlar/202401/01012024.xml
        year_month = current.strftime('%Y%m')  # Ornek: 202401
        day_month_year = current.strftime('%d%m%Y')  # Ornek: 01012024
        url = f"https://www.tcmb.gov.tr/kurlar/{year_month}/{day_month_year}.xml"
        
        try:
            # XML dosyasi indirildi
            response = requests.get(url, timeout=10)
            
            # XML parse edildi
            root = ET.fromstring(response.content)
            
            # XML icindeki her Currency elementi islendi
            for currency in root.findall("Currency"):
                
                # Para birimi kodu alindi (EUR, USD, GBP, vb)
                code = currency.get("CurrencyCode")
                
                # Sadece istenen para birimleri alindi
                if code in ["EUR", "GBP", "USD"]:
                    
                    # ForexSelling (satis kuru) degeri alindi
                    # Not: TCMB virgul kullanir, nokta ile degistirildi
                    rate_text = currency.find("ForexSelling").text
                    rate = float(rate_text.replace(",", "."))
                    
                    # Veri listeye eklendi
                    all_data.append({
                        "Date": current.strftime("%Y-%m-%d"),
                        "Currency": code,
                        "Rate": round(rate, 4)
                    })
            
            # TRY manuel olarak eklendi (her zaman 1.0)
            # Not: TRY XML'de olmadigi icin elle ekleniyor
            all_data.append({
                "Date": current.strftime("%Y-%m-%d"),
                "Currency": "TRY",
                "Rate": 1.0
            })
            
            print(f"{current} - OK")
            
        except Exception as e:
            # Veri yoksa veya hata olussa bildirildi
            # Not: Haftasonu veya resmi tatil gunleri veri olmaz
            print(f"{current} - VERI YOK")
        
        # Bir sonraki gune gecildi
        current += timedelta(days=1)
    
    # Liste DataFrame'e cevrildi
    return pd.DataFrame(all_data)


# main program
if __name__ == "__main__":
    
    # Tarih araligi belirlendi
    start_date = "2024-01-01"
    end_date = "2024-01-31"
    
    print(f"Doviz kurlari cekiliyor: {start_date} - {end_date}")
    print("-" * 10)
    
    # Kurlar cekildi
    df = get_fx_rates(start_date, end_date)
    
    # Excel dosyasina kaydedildi
    output_file = "fx_rates.xlsx"
    df.to_excel(output_file, index=False)
    
    # Ozet bilgi yazdirildi
    print("-" * 10)
    print(f"Toplam kayit sayisi: {len(df)}")
    print(f"Dosya kaydedildi: {output_file}")
    print(f"\nIlk 10 kayit:")
    print(df.head(10))