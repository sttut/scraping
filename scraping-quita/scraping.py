from selenium import webdriver  
from selenium.webdriver.common.by import By  # 要素の選択用
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()  # webdriverの指定(Chrome)

url = "https://qiita.com/"  # スクレイピングしたいサイトのURL
driver.get(url)

titles = []
urls = []

# driverで要素を探索
# [ driver.find_element ] or [ find_elements ] 
# 前者は単一の要素もしくは初めに見つけた要素のみ、後者は複数の要素を探索

# スクレイピングしたい要素が入った記事全体の取得
articles = driver.find_elements(By.CLASS_NAME, "style-1w7apwp")

# それでは、articlesの全ての記事のタイトルとURLを配列に納めていきます
# Quitaの記事のブロックの最上位のclass[style-1w7apwp]でブロックごと取得し、ブロック分ぶん回す
for article in articles:

    title = article.find_element(By.TAG_NAME, "h2").text
    url = article.find_element(By.CLASS_NAME, "style-2vm86z").get_attribute("href")

    titles.append(title)
    urls.append(url)

# タイトルとURLの標準出力
# for i in range(len(titles)):
    # print(titles[i], urls[i])

# 以下CSV作成
datas = ""

# csv形式に変換
for i in range(len(titles)):
    datas += titles[i] + ", " + urls[i] + "\n"

# ファイルの作成
with open("scraping-quita\\datas.csv", "w") as file:
    file.write(datas)
