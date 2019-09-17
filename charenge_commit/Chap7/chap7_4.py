numbers = [10, 20, 4, 34]

while True:
    answer = input("Number guessing game")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please enter a number or 'q'")

    if answer in numbers:
        print("Is the correct answer")
        break
    else:
        print("Incorrect answer")
