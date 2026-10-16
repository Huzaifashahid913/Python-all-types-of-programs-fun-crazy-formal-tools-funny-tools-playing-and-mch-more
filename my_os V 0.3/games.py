import difflib
import random
import re
import time
import pyjokes
from common import ask, ask_int, ask_choice, ask_yes_no, heading, line


def guess_the_number():
    heading("GUESS THE NUMBER")
    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0
    started = time.monotonic()
    print(f"I'm thinking of a number from {low} to {high}. Type exit to return.")
    while True:
        guess = ask_int("Your guess: ", low, high)
        attempts += 1
        if guess == secret:
            print(f"\n  🎉 You got it! The number was {secret}.")
            print(f"  Attempts: {attempts}  |  Time: {time.monotonic() - started:.1f} seconds")
            return
        print("  Too high. Go lower!" if guess > secret else "  Too low. Go higher!")
        if attempts == 5:
            print(f"  Hint: the number is {'even' if secret % 2 == 0 else 'odd'}.")
        elif attempts == 8:
            print(f"  Extra hint: it is {'above' if secret > 50 else '50 or below'} 50.")


def snake_water_gun():
    heading("SNAKE • WATER • GUN")
    print("Snake drinks water • Water sinks gun • Gun shoots snake")
    rounds = ask_int("How many rounds (1–20)? ", 1, 20)
    wins = losses = draws = 0
    beats = {"snake": "water", "water": "gun", "gun": "snake"}
    for turn in range(1, rounds + 1):
        print(f"\nROUND {turn}/{rounds}")
        player = ask_choice("Choose snake, water, or gun: ", {
            "snake": ["s", "sn", "serpent"],
            "water": ["w", "wa", "drink"],
            "gun": ["g", "shoot", "weapon"],
        }, retry_message="Type snake (s), water (w), or gun (g).")
        computer = random.choice(tuple(beats))
        if player == computer:
            result = "DRAW"
            draws += 1
        elif beats[player] == computer:
            result = "YOU WIN!"
            wins += 1
        else:
            result = "COMPUTER WINS"
            losses += 1
        line()
        print(f"  Your choice     : {player.title()}")
        print(f"  Computer choice : {computer.title()}")
        print(f"  Round result    : {result}")
        line()
    heading("FINAL SCORE")
    print(f"  You: {wins} wins  |  Computer: {losses} wins  |  Draws: {draws}")
    print("  Overall: YOU WIN!" if wins > losses else "  Overall: COMPUTER WINS" if losses > wins else "  Overall: IT'S A DRAW")


def tic_tac_toe():
    heading("TIC-TAC-TOE")

    board = [str(i) for i in range(1, 10)]

    wins = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def show():
        print(
            f"\n  {board[0]} | {board[1]} | {board[2]}\n"
            " ---+---+---\n"
            f"  {board[3]} | {board[4]} | {board[5]}\n"
            " ---+---+---\n"
            f"  {board[6]} | {board[7]} | {board[8]}\n"
        )

    def available_moves():
        return [
            i for i, cell in enumerate(board)
            if cell not in ("X", "O")
        ]

    def winning_move(player):
        for combo in wins:
            values = [board[i] for i in combo]

            if values.count(player) == 2:
                empty = [
                    i for i in combo
                    if board[i] not in ("X", "O")
                ]

                if len(empty) == 1:
                    return empty[0]

        return None

    def creates_fork(move, player):
        # Temporarily test a move to see how many
        # different winning moves it creates.
        board[move] = player

        winning_options = 0

        for next_move in available_moves():
            board[next_move] = player

            if any(
                all(board[i] == player for i in combo)
                for combo in wins
            ):
                winning_options += 1

            board[next_move] = str(next_move + 1)

        board[move] = str(move + 1)

        return winning_options >= 2

    def computer_move():
        available = available_moves()

        # 1. Win immediately if possible.
        move = winning_move("O")
        if move is not None:
            return move

        # 2. Block the player's immediate win.
        move = winning_move("X")
        if move is not None:
            return move

        # 3. Create a fork to make two winning threats.
        for move in available:
            if creates_fork(move, "O"):
                return move

        # 4. Block the player's possible fork.
        for move in available:
            if creates_fork(move, "X"):
                return move

        # 5. Take the center.
        if 4 in available:
            return 4

        # 6. Take an available corner.
        corners = [i for i in (0, 2, 6, 8) if i in available]
        if corners:
            return random.choice(corners)

        # 7. Take a side square.
        sides = [i for i in (1, 3, 5, 7) if i in available]
        if sides:
            return random.choice(sides)

    print("You are X. The computer is O. Pick a square from 1 to 9.")

    while True:
        show()

        move = ask_int("Your square: ", 1, 9) - 1

        if board[move] in ("X", "O"):
            print("  That square is taken. Choose another.")
            continue

        board[move] = "X"

        if any(
            all(board[p] == "X" for p in combo)
            for combo in wins
        ):
            show()
            print("  You beat the computer! 🏆")
            return

        if not available_moves():
            show()
            print("  Draw! Nobody won this round.")
            return

        move = computer_move()
        board[move] = "O"

        print(f"  Computer chose square {move + 1}.")

        if any(
            all(board[p] == "O" for p in combo)
            for combo in wins
        ):
            show()
            print("  The computer won. Try again!")
            return

        if not available_moves():
            show()
            print("  Draw! Nobody won this round.")
            return

def word_scramble():
    heading("WORD SCRAMBLE")
    words = ["python", "keyboard", "developer", "internet", "function", "variable", "computer", "program", "browser", "creative", "algorithm", "animation", "terminal", "database", "pyramid"]
    points = 0
    for round_no in range(1, 6):
        word = random.choice(words)
        scrambled = word
        while scrambled == word:
            scrambled = "".join(random.sample(word, len(word)))
        print(f"\nRound {round_no}/5: unscramble  ➜  {scrambled.upper()}")
        answer = ask("Your answer: ").lower()
        if answer == word:
            points += 10
            print("  Correct! +10 points ✨")
        else:
            print(f"  Not this time. Word: {word}")
    print(f"\n  Final score: {points}/50")


def hangman():
    heading("HANGMAN — WORD GUESSING")
    words = ["python", "banana", "laptop", "coding", "rocket", "puzzle", "planet", "browser", "school", "guitar"]
    word = random.choice(words)
    guessed = set()
    wrong = 0
    max_wrong = 7
    while wrong < max_wrong:
        shown = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"\n  Word: {shown}    Wrong guesses: {wrong}/{max_wrong}")
        if all(ch in guessed for ch in word):
            print("  You saved the stick figure! 🎉")
            return
        letter = ask("Guess one letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("  Enter exactly one letter.")
        elif letter in guessed:
            print("  You already tried that letter.")
        elif letter in word:
            guessed.add(letter)
            print("  Nice! That letter is in the word.")
        else:
            guessed.add(letter)
            wrong += 1
            print("  Nope! Try another.")
    print(f"  Game over! The word was: {word}")


def math_sprint():
    heading("MATH SPRINT")
    questions = ask_int("How many questions (1–20)? ", 1, 20)
    score = 0
    started = time.monotonic()
    for i in range(1, questions + 1):
        a, b = random.randint(2, 20), random.randint(2, 12)
        op = random.choice(("+", "-", "×"))
        answer = a + b if op == "+" else a - b if op == "-" else a * b
        raw = ask(f"  {i:02}/{questions:02}  {a} {op} {b} = ")
        try:
            if int(raw) == answer:
                score += 1
                print("  Correct!")
            else:
                print(f"  Answer: {answer}")
        except ValueError:
            print(f"  Please remember the answer was {answer}.")
    elapsed = time.monotonic() - started
    print(f"\n  Score: {score}/{questions}  |  Time: {elapsed:.1f}s")


def answer_matches(response, accepted):
    clean = lambda value: " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())
    response = clean(response)
    if not response:
        return False
    answers = [clean(value) for value in accepted]
    if response in answers:
        return True
    if len(response) >= 5 and any(answer.startswith(response) for answer in answers):
        return True
    if len(response) >= 5:
        return any(difflib.SequenceMatcher(None, response, answer).ratio() >= 0.84 for answer in answers if len(answer) >= 5)
    return False


def jeeto_pakistan():
    heading("JEETO PAKISTAN QUIZ")
    questions = [
        ("Who is commonly credited with developing the practical incandescent light bulb?", ["thomas edison", "thomas alva edison", "thomas"], "Thomas Edison"),
        ("Who co-founded Facebook?", ["mark zuckerberg", "mark"], "Mark Zuckerberg"),
        ("Who is the CEO of Anthropic?", ["dario amodei", "dario"], "Dario Amodei"),
        ("Largest city in Pakistan by population?", ["karachi"], "Karachi"),
        ("How many continents are in the common seven-continent model?", ["7", "seven", "seven continents"], "7"),
        ("What is the capital of Japan?", ["tokyo"], "Tokyo"),
        ("What does CPU stand for?", ["central processing unit"], "Central Processing Unit"),
        ("How many sides does a hexagon have?", ["6", "six"], "Six"),
    ]
    random.shuffle(questions)
    score = 0
    for i, (question, accepted, answer) in enumerate(questions[:5], 1):
        print(f"\nQuestion {i}/5 • 10 points")
        response = ask(question + "\n  Answer: ").lower().strip(" .!?")
        if answer_matches(response, accepted):
            score += 10
            print("  ✅ Correct! +10")
        else:
            print(f"  ❌ Correct answer: {answer}")
    correct = score // 10
    heading("QUIZ RESULT")
    print(f"  Correct answers: {correct}/5  |  Score: {score}/50")
    print(f"  Fantasy prize: ${correct * 3:,} million — just for fun, no real money!")


def magic_8_ball():
    heading("MAGIC 8-BALL")
    answers = ["Absolutely!", "Definitely yes.", "The vibes are good.", "Ask again in a minute.", "I can't reveal that yet.", "Maybe...", "My sources say no.", "Absolutely not.", "It is looking suspicious.", "Trust your brain, not the ball.", "The answer is hidden in snacks.", "404: Future not found."]
    while True:
        question = ask("Ask a yes/no question (or type done): ")
        if question.lower().strip() in ("done", "stop", "finished", "that's all", "thats all"):
            return
        print("  🎱 " + random.choice(answers))


def dice_roller():
    heading("DICE ROLLER")
    while True:
        sides = ask_int("Number of sides (2–100, 0 to stop): ", 0, 100)
        if sides == 0:
            return
        if sides < 2:
            print("  A die needs at least 2 sides.")
            continue
        count = ask_int("How many dice (1–20)? ", 1, 20)
        rolls = [random.randint(1, sides) for _ in range(count)]
        print(f"  Rolls: {rolls}  |  Total: {sum(rolls)}")


def coin_toss():
    heading("COIN TOSS")
    count = ask_int("How many coin flips (1–100)? ", 1, 100)
    flips = [random.choice(("Heads", "Tails")) for _ in range(count)]
    heads, tails = flips.count("Heads"), flips.count("Tails")
    print("\n  " + " • ".join(flips))
    print(f"\n  Heads: {heads}  |  Tails: {tails}")


def random_picker():
    heading("RANDOM PICKER")
    print("Enter choices separated by commas.")
    raw = ask("Choices: ")
    choices = [item.strip() for item in raw.split(",") if item.strip()]
    if len(choices) < 2:
        print("  Please provide at least two choices separated by commas.")
        return
    print(f"\n  🥁 The winner is: {random.choice(choices)}")


def joke_teller():
    heading("JOKE TELLER")
    jokes = pyjokes.get_jokes()
    mode = ask_choice("One joke or jokes (three)? ", {
        "one": ["joke", "single", "just one", "1", "one joke"],
        "three": ["jokes", "multiple", "several", "3", "three jokes", "more jokes"],
    }, retry_message="Type joke/one or jokes/three.")
    batch = random.sample(jokes, k=1 if mode == "one" else 3)
    for index, joke in enumerate(batch, 1):
        print(f"\n  {index}. {joke}")
    try:
        speak = ask_yes_no("\nRead them aloud too? (y/n): ", default=False)
    except Exception:
        raise
    if speak:
        try:
            import pyttsx3
            voice = pyttsx3.init()
            voice.say(" ".join(batch))
            voice.runAndWait()
        except ImportError:
            print("  Voice needs the optional package. Run install_optional.bat.")
        except Exception as exc:
            print(f"  Voice feature isn't available here: {exc}")
