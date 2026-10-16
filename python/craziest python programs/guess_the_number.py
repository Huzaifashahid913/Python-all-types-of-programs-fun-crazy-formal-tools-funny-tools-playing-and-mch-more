def play():
    import time
    import random

    cc = random.randint(1, 100)

    i = 0

    start_time = time.time()

    while True:
        mc = input("Guess the between 1 to 100 or 'exit' for exit: ").lower()
        if mc == "exit":
            exit()
        mc = int(mc)
        if mc == cc:
            print(f"Congrats!You got it the number was: {cc}")
            break
        elif mc == "exit":
            exit()
        elif mc > cc:
            print("Guess some Lower!")
        elif mc < cc:
            print("Guess some Higher!")
        i += 1

    end_time = time.time()

    print(f"You got it in {i} attempts in {round(end_time-start_time, 2)} seconds ")

if __name__ == "__main__":
    play()