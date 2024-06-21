import requests
from bs4 import BeautifulSoup
import pandas as pd

# 設定要抓取的Yahoo Finance科技新聞網址
url = 'https://finance.yahoo.com/tech/'

# 發送請求
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 解析新聞資料
articles = soup.find_all('h3', class_='Mb(5px)')

news_list = []

for article in articles:
    title = article.get_text()
    link = 'https://finance.yahoo.com' + article.find('a')['href']
    news_list.append({'title': title, 'link': link})

# 將資料存儲到DataFrame中
df = pd.DataFrame(news_list)

# 將資料匯出成CSV檔案
csv_file_path = "tech_stock_market_news.csv"
df.to_csv(csv_file_path, index=False)

print(f"新聞資料已匯出至 {csv_file_path}")
