import os
import requests

# IEEE Xplore APIのエンドポイントとパラメータを設定する
url = 'https://ieeexploreapi.ieee.org/api/v1/search/articles'
api_key = ''
headers = {
    'X-API-Key': api_key,
    'Content-Type': 'application/json'
}
params = {
    'querytext': 'Federated Learning',  # 検索キーワードを指定する
    'max_records': 30,  # 取得する論文数を指定する
    'sort_order': 'desc',  # 降順でソートする
    'sort_field': 'publication_year'  # 発行年でソートする
}

# IEEE Xplore APIから論文情報を取得する
response = requests.post(url, headers=headers, json=params)
data = response.json()['articles']

# 論文をダウンロードする
folder = 'C:/Users/~'
for article in data:
    title = article['title']
    abstract = article['abstract']
    if 'Federated Learning' in title or 'Federated Learning' in abstract:
        pdf_url = article['pdf_url']
        response = requests.get(pdf_url)
        filename = f"{title}.pdf"
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"{filename} saved to {folder}")
