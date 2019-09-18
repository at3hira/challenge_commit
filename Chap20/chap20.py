import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

class YahooScraper:
    def __init__(self, site):
        self.site = site


    def scraper(self):
        """
        HTMLパーサー
        
        :return sp : パースしたhtml
        """
        ssl._create_default_https_context = ssl._create_unverified_context # Python2.7.9以降　SSLエラー対応
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html, "html.parser") # BeautifulSoupオブジェクト作成
        return sp


    def change_url(self, url):
        """
        インスタンス変数を変更する
        """
        self.site = url
 

    def pickup(self, html):
        """
        Yahooトップからピックアップニュースのurlを取得してリストで返却

        :param html : パースしたhtml
        :return url_list : ニュースのurlリスト
        """
        url_list = []
        topic_list = html.select("div.topicsList")[0]

        for ps in topic_list.find_all("a"):
            url = ps.get("href")
            if url is None:
                continue

            if "pickup" in url:
                url_list.append(url)

        return url_list


    def news_contents(self, html):
        """
        取得したurlから必要な項目を抜き出しファイルに書き出す
        
        :param html : パースしたhtml
        """
        with open("yahoo_pickup.txt", "a") as f:
            for tag in html.find_all("article"):
                title = tag.select('h1.tpcHeader_title')[0].text # 記事タイトル
                date = tag.select('p.tpcHeader_date')[0].text # 配信時間
                summary = tag.select('p.tpcNews_summary')[0].text # 要約
                news_link = tag.select('div.tpcNews_header a')[0].get('href') # 記事リンク
                
                if title is None and date is None and summary is None and news_link:
                    continue
                else:
                    print("\n" + title + " : " +news_link + "\n" + summary + "\n" + date)
                    f.write("\n" + title + " : " +news_link + "\n" + summary + "\n" + date)


news = "https://news.yahoo.co.jp/categories/entertainment"

sc = YahooScraper(news)
pickup_parser = sc.scraper()
pickup_list = sc.pickup(pickup_parser)

for pickup_url in pickup_list:
    sc.change_url(pickup_url)
    news_parser = sc.scraper()
    sc.news_contents(news_parser)
