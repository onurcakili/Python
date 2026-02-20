import pandas as pd
import requests
from datetime import datetime

SHOP_NAME = "xxx"  # Your Shopify store name
ACCESS_TOKEN = "xxx"  # Admin API access token

start_date = "2026-01-01"
end_date = "2026-01-30"

url = f"https://{SHOP_NAME}.myshopify.com/admin/api/2024-01/orders.json"

headers = {
    "X-Shopify-Access-Token" : ACCESS_TOKEN,
    "Content-Type" : "application/json"
}

params = {
    "status" : "any",
    "limit" : 250,
    "created_at_min" : start_date,
    "created_at_max" : end_date
}


response = requests.get(url, headers=headers, params=params)
orders = response.json()["orders"]

df_all_orders = pd.DataFrame(orders)


def extract_nested_table(orders, nested_column):
    nested_tables = []
    
    for order in orders:
        order_id = order["id"]
        nested_table = order.get(nested_column, [])    ## nested_table = order["line_items"]    -> sözlük.get(anahtar, varsayılan_değer)
        
        # Skip if not a list
        if not isinstance(nested_table, list):    ##isinstance(nested_table, list) → "items bir liste mi?" diye soruyor
            continue
            
        # Add order_id to each nested item
        for table in nested_table:
            table["order_id"] = order_id
            nested_tables.append(table)
    
    return pd.json_normalize(nested_tables) if nested_tables else pd.DataFrame()

df_orders = df_all_orders.drop(columns=["line_items", "refunds", "shipping_lines", "tax_lines", "discount_codes"])

df_line_items = extract_nested_table(orders, "line_items")

df_refunds = extract_nested_table(orders, "refunds")


