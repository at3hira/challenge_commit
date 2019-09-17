"""
２重のリストになっている要素をカンマ区切りでCSVファイルに書き出す
"""

import csv
list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "Man on Fire"]]

with open("chap9_3.csv", "w") as csv_obj:
    csv_file = csv.writer(csv_obj, delimiter=",")
    for movies in list:
        csv_file.writerow(movies)