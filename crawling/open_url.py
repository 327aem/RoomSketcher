import pandas as pd
import webbrowser
import openpyxl
filename = "C:/Users/준영/쿠팡_products_list_TV.xlsx"
df = pd.read_excel(filename, engine='openpyxl')
link = df['product_url']

for idx, url in enumerate(link):
    webbrowser.open(url)
    if idx == 50 :
        break