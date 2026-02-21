import requests
import pandas as pd


# Ayarlar
ACCESS_TOKEN = "x"  
AD_ACCOUNT_ID = "x"  # örn: act_123456789

# Çekilecek metrikler
params = {
    "fields": "campaign_name,impressions,clicks,spend,reach",
    "date_preset": "last_7d",  # son 7 gün
    "level": "campaign",
    "access_token": ACCESS_TOKEN,
}

# API isteği
url = f"https://graph.facebook.com/v19.0/{AD_ACCOUNT_ID}/insights"

response = requests.get(url, params=params)

data = response.json()["data"]

df_meta_ads = pd.DataFrame(data)

df_meta_ads
