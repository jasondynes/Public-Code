import requests
from bs4 import BeautifulSoup


TRACK_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD"

headers = {
    'Accept': 'text/plain',
    'Accept-Charset': 'utf-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB',
    #'Cache-Control': 'max-age=0',
    #'Content-Length': '1708',
    #'Content-Type': 'application/pdf',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",

}
response = requests.get(TRACK_URL, headers=headers)
charts_web_page = response.text

soup = BeautifulSoup(charts_web_page, "html.parser")

# complete price embedded and can be extracted alternative way
full_price = soup.find(class_="a-offscreen").get_text()

# scraped separately via multiple elements
price_currency = soup.find(class_="a-price-symbol").getText()
price_main = soup.find(class_="a-price-whole").getText()
price_fraction = soup.find(class_="a-price-fraction").getText()

# scraped separately via multiple elements
price = float(price_main + price_fraction)
print(f"{price_currency}{price_main}{price_fraction}")
print(price)

# complete price embedded and can be extracted alternative way
print(full_price)