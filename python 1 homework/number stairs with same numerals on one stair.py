__author__ = 'Trunishka'
user_in = input("insert the number of stairs")
try:
    number = int(user_in)
    if number > 0:
        for i in range(number + 1):
            numerals = str(i)
            print(numerals * i)
    else:
        print("the number must be more than zero")
except ValueError:
    print("insert only integer")
print("Finish")
