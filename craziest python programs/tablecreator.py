
def play():
    number = int(input("enter the number you want to write table: "))
    times_number = int(input("Enter how much times you want: "))
    try:
        def CreateTable(number = number, times = times_number):
            for i in range(times):
                print(number," x ", i+1, "=", number*(i+1))
            return print(f'\n the table of {number},  is finished \n')
    except:
        print("it's look like you entered a string please enter a number")
    CreateTable()

if __name__ == "__main__":
    play()