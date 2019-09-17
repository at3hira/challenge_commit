"""
質問に対する回答をファイルに書き出す
何も入力しなかった場合はアラートを出し再度、入力させる
"""

flg = True
while flg == True:
    answer = input("What is your favorite movie?")

    if not answer:
        print("Enter your favorite movie")
    else:
        break

with open("chap9_2_answer.txt", "w") as file_obj:
    text = file_obj.write(answer)
