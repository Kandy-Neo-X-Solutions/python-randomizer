import random
#number = random.randint(1,100)
#print(number)

number1 = int(input("Enter first your number"))
number2 = int(input("Enter second your number"))
if number2 < number1:
    print("ERROR: first number must be smaller")
else:
    randomizer = random.randint(number1,number2)
    print(randomizer)

