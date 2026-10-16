import secrets
def play():
    fop = open("results.txt", "w")

    def main():
        global win
        win = "No one!"
        global rules
        rules = input("""\n===================================================================\nHey!Welcome to the game read the rules given below and start gaming: \n1. snake drinks water\n2. gun shoots the snake\n3. water sinks the gun\n=======================\n\nwrite "agree" if you agree: """).lower()
        if (rules == "agree"):
            global my_choice
            my_choice = input("\n==================================================\nEnter one of these exactly (snake, water, or gun): ").lower()

            s = "snake"
            w = "water"
            g = "gun"

            game = ["snake", "water", "gun", "gun", "water", "snake", "snake" "gun", "water"]
            global ra
            ra = secrets.choice(game)

            if(my_choice == ra):
                win = "Draw!"
                print(f"\nIt's draw! i chosed the same")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")

            elif(my_choice == s and ra == w):
                win = "You!"
                print(f"\nCongrats! you won the game!")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")
            elif(my_choice == s and ra == g):
                win = "Computer!"
                print(f"\nOH no! you lose that.")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")

            elif(my_choice == w and ra == g):
                win = "You!"
                print(f"\nCongrats! you won the game!")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")
            elif(my_choice == w and ra == s):
                win = "Computer!"
                print(f"\nOH no! you lose that.")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")

            elif(my_choice == g and ra == w):
                win = "Computer!"
                print(f"\nOH no! you lose that.")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")
            elif(my_choice == g and ra == s):
                win = "you!"
                print(f"\nCongrats! you won the game!")
                print(f"_______________________\nComputer_choice: {ra}")
                print(f"Your_choice: {my_choice}\nWinner: {win}\n======================")
            else:
                print("\nActualy input was incorrect, write exactly your choice without leaving any space before and after and hit enter")
        else:
            print("\nOK! It's your choice and up to you.")
        return win

    my_choice = ""
    rules = ""
    times = int(input("How much times you want to play: "))

    for i in range(times):
        if (my_choice == "exit" or rules == "exit"):
            exit()
        main()
        fop.write(f"\nResult of round {i+1} \n_______________________\nComputer_choice: {ra}\nYour_choice: {my_choice}\nFinal result: {win}\n======================")
    else:
        print("\nGame ended check results.txt to see all the results")
    fop.close()

if __name__ == "__main__":
    play()