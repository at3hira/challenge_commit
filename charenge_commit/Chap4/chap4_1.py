"""
Take input integer Returns it multiplied by 2

param num: int
return x: multiplication * 2
"""
def f(num):
    x = num ** 2
    return x

num = input("type number")
num = int(num)

result = f(num)
print(result)
