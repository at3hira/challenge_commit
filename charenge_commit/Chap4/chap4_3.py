"""
Create fuction for two optional params
and three required params
3つの必須引数と2つのオプション引数を出力する関数を作成

param a: int
param b: int
param c: int
param d: int
param e: int
return: int
"""
def test_3(a, b, c, d=9, e=7):
    return a + b + c + d + e

result = test_3(3, 2, 4)
print(result)
