"""
２重のリストになっている要素をカンマ区切りでCSVファイルに書き出す
"""

import csv
list = [["トップガン", "卒業白書", "マイノリティ・リポート"], ["タイタニック", "マイ・ボディガード"]]

with open("chap9_4.csv", "w", encoding="utf-8") as csv_obj:
    csv_file = csv.writer(csv_obj, delimiter=",")
    for movies in list:
        csv_file.writerow(movies)
