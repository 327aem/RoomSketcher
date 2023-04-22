import requests
from bs4 import BeautifulSoup
import pandas as pd

def coupang_product(keyword,pages):
    baseurl = 'https://www.coupang.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3" #이 문장 추가해야만 쿠팡 크롤링 정상 작동
    }
    
    products_link = []
    for page in range(1,pages+1):
        url = f'https://www.coupang.com/np/search?q={keyword}&channel=user&sorter=scoreDesc&listSize=36&isPriceRange=false&rating=0&page={page}&rocketAll=false'

        response = requests.get(url, headers=headers)
        print("1")
        soup = BeautifulSoup(response.content, 'html.parser')
        products_lis = soup.find('ul', id='productList').find_all('li')
        for li in products_lis:
            a_link = li.find('a', href=True)['href']
            prd_link = baseurl + a_link
            prd_name = li.find('div', class_='name').text
            prd_img = li.find('img')['src']
            try:
                base_price = li.find('span', class_='price-info').find('del', class_='base-price').text
            except :
                base_price = ''
            price = li.find('strong', class_='price-value').text
            
            products_info = {
                'name' : prd_name,
                'base_price' : base_price,
                'price' : price,
                'product_url' : prd_link,
                'product_img' : prd_img,
                'product_label' : keyword
            }
            products_link.append(products_info)
    
    print(len(products_link))
    df = pd.DataFrame(products_link)
    print(df)
    df.to_csv('쿠팡_products_list_TV.csv', index=False, encoding='utf-8-sig')
    
if __name__ == '__main__':
    coupang_product('TV',3) #keyword의 page까지 크롤링
    