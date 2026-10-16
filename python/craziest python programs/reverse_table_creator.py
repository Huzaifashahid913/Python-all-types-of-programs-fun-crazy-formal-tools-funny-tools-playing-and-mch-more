def play():
    number = int(input("Enter wanted number: "))
    times = int(input("How much times: "))

    def table(num = number, times = times):
        for i in range(times):
            print(f"{num} x {times-(i)} = {num*(times-(i))}")

    table()

if __name__ == "__main__":
    play()