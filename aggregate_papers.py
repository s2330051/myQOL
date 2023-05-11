import os
import requests
import feedparser
import re

# arXiv APIのエンドポイントとパラメータを設定する
url = 'http://export.arxiv.org/api/query'
params = {
    'search_query': 'Federated Learning OR federated learning',  # 検索キーワードを指定する
    'max_results': 50,  # 取得する論文数を指定する
    'sortBy': 'lastUpdatedDate',  # 更新日時でソートする
    'sortOrder': 'descending'  # 降順でソートする
}

# arXiv APIから論文情報を取得する
response = requests.get(url, params=params)
feed = feedparser.parse(response.text)

# 論文をダウンロードする
folder = 'C:/Users/~'
for entry in feed.entries:


    pdf_url = entry.links[1].href  # PDFのURLを取得する
    response = requests.get(pdf_url)

    # ダウンロードしたPDFをローカルフォルダに保存する
    title = re.sub(r'[\\/*?:"<>|]+', '', entry.title)


    if 'Federated Learning' in entry.title:
        filename = f"{title}.pdf"
        filename = filename.replace('\n', '')  # 改行文字を削除する
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"{filename} saved to {folder}")
