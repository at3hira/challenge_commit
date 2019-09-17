"""
Function to convert str to float

:param x str
:return x converted to float

"""
def conv_float(x):
    try:
        return float(x)
    except ValueError:
        print("Invalid string")

float_input = input("Float Input")
result = conv_float(float_input)
print(result)
