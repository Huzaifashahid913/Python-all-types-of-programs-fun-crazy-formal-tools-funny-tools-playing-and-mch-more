
def play():
    n = int(input("How much piramids want: "))
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        print("*" * (2*i-1), end="")
        print("")

if __name__ == "__main__":
    play()