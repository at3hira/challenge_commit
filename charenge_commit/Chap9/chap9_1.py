# 別階層にあるファイルを読み込む
import os

file_path = os.path.join("../", "tstp", "chap9_test.txt")

with open(file_path, "r", encoding="utf-8") as file_obj:
    print(file_obj.read())
