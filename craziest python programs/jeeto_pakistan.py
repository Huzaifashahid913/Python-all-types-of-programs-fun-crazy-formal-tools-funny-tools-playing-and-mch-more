import requests


def play():
    qone = input("Who invented bulb: ").lower()
    qtwo = input("Who made facebook: ").lower()
    qthree = input("Who is the CEO of Anthropic/Claude: ").lower()
    qfour = input("Which is the biggest city in Pakistan: ").lower()
    qfive = input("How many continents are there in the world: ").lower()

    point = 0

    if (qone == "thomus" or qone == "thomus edison"):
        point = point+10
    if (qtwo == "mark" or qtwo == "mark zuckerberg"):
        point = point+10
    if (qthree == "dario" or qthree == "dario amodei"):
        point = point+10
    if (qfour == "karachi"):
        point = point+10
    if (qfive == "7" or qfive == "seven"):
        point = point+10

    print("you got only", point//10,"correct so you won: ",(((point*100)//50)//10)*3, "million dollar")


if __name__ == "__main__":
    play()