
my_info = {"height" : 180, "color" : "navy", "gender" : "man"}
my = input("Input height, color, gender")

if my in my_info:
    my_data = my_info[my]
    print(my_data)
else:
    print("No data")
    
