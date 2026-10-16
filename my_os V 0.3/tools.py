import ast
import base64
import math
import operator
import os
import secrets
import string
import time
import webbrowser
from urllib.parse import urlparse
from common import ask, ask_int, ask_choice, ask_yes_no, heading, line, data_path


def calculator():
    heading("SMART CALCULATOR")
    print("Use numbers and + - * / // % ** with parentheses. Example: (12 + 3) * 2")
    print("For safety, this calculator accepts arithmetic only, not Python code.")
    operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
                 ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
                 ast.Mod: operator.mod, ast.Pow: operator.pow, ast.UAdd: operator.pos,
                 ast.USub: operator.neg}

    def calculate(node):
        if isinstance(node, ast.Expression):
            return calculate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](calculate(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            left, right = calculate(node.left), calculate(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("Power is too large.")
            if abs(left) > 10**100 or abs(right) > 10**100:
                raise ValueError("Number is too large.")
            return operators[type(node.op)](left, right)
        raise ValueError("Only basic arithmetic is allowed.")

    while True:
        expression = ask("Expression (or exit): ")
        try:
            if len(expression) > 180:
                raise ValueError("Expression is too long.")
            result = calculate(ast.parse(expression, mode="eval"))
            if isinstance(result, float) and (not math.isfinite(result)):
                raise ValueError("Result is outside the usable range.")
            print(f"  = {result:g}" if isinstance(result, float) else f"  = {result}")
        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError) as exc:
            print(f"  Can't calculate that: {exc}")


def reverse_table_creator():
    heading("REVERSE MULTIPLICATION TABLE")
    number = ask_int("Enter the number: ")
    times = ask_int("How many rows (1–100)? ", 1, 100)
    line()
    for multiplier in range(times, 0, -1):
        print(f"  {number:>7} × {multiplier:<3} = {number * multiplier}")
    line()


def star_pyramids():
    heading("STAR PATTERN STUDIO")
    print("1. Pyramid   2. Inverted pyramid   3. Square   4. Right triangle")
    choice = ask_choice("Pattern: ", {
        "1": ["pyramid", "normal pyramid", "triangle pyramid", "1"],
        "2": ["inverted pyramid", "upside down pyramid", "reverse pyramid", "2"],
        "3": ["square", "box", "block", "3"],
        "4": ["right triangle", "triangle", "left triangle", "4"],
    }, retry_message="Try pyramid, inverted pyramid, square, or triangle.")
    size = ask_int("Size (1–40): ", 1, 40)
    print()
    for row in range(1, size + 1):
        if choice == "1":
            print(" " * (size - row) + "*" * (row * 2 - 1))
        elif choice == "2":
            print(" " * (row - 1) + "*" * (2 * (size - row) + 1))
        elif choice == "3":
            print("*" * size)
        else:
            print("*" * row)
    print()


def unit_converter():
    heading("UNIT CONVERTER")
    print("1. Kilometres ↔ miles   2. Kilograms ↔ pounds   3. Celsius ↔ Fahrenheit")
    choice = ask_choice("Choose conversion: ", {
        "1": ["distance", "dist", "kilometres", "kilometers", "miles", "km", "1"],
        "2": ["weight", "wt", "mass", "kilograms", "pounds", "kg", "lb", "2"],
        "3": ["temperature", "temp", "celsius", "fahrenheit", "degrees", "3"],
    }, retry_message="Try distance, weight, or temperature.")
    while True:
        raw = ask("Enter value (number): ")
        try:
            value = float(raw)
            if not math.isfinite(value):
                raise ValueError
            break
        except ValueError:
            print("  That isn't a valid finite number. Try again.")
    if choice == "1":
        print(f"  {value:g} km = {value * 0.621371:g} miles")
        print(f"  {value:g} miles = {value / 0.621371:g} km")
    elif choice == "2":
        print(f"  {value:g} kg = {value * 2.2046226218:g} lb")
        print(f"  {value:g} lb = {value / 2.2046226218:g} kg")
    else:
        print(f"  {value:g}°C = {(value * 9 / 5) + 32:g}°F")
        print(f"  {value:g}°F = {(value - 32) * 5 / 9:g}°C")


def text_analyzer():
    heading("TEXT ANALYZER")
    text = ask("Paste text to analyze: ", strip=False)
    words = text.split()
    letters = sum(char.isalpha() for char in text)
    digits = sum(char.isdigit() for char in text)
    spaces = sum(char.isspace() for char in text)
    punctuation = sum(not char.isalnum() and not char.isspace() for char in text)
    print("\n  TEXT REPORT")
    line()
    print(f"  Characters (with spaces) : {len(text)}")
    print(f"  Characters (no spaces)   : {len(text) - spaces}")
    print(f"  Words                    : {len(words)}")
    print(f"  Letters                  : {letters}")
    print(f"  Digits                   : {digits}")
    print(f"  Spaces                   : {spaces}")
    print(f"  Punctuation/symbols      : {punctuation}")
    print(f"  Uppercase                : {sum(ch.isupper() for ch in text)}")
    print(f"  Lowercase                : {sum(ch.islower() for ch in text)}")
    print(f"  Reversed                 : {text[::-1]}")
    line()


def secret_text():
    heading("SECRET TEXT — BASE64")
    print("1. Encode text   2. Decode text")
    print("Note: Base64 is reversible encoding, NOT secure encryption.")
    choice = ask_choice("Choose: ", {
        "1": ["encode", "encrypt looking text", "make secret", "encode text", "1"],
        "2": ["decode", "decrypt", "decode text", "read secret", "2"],
    }, retry_message="Type encode or decode.")
    if choice == "1":
        text = ask("Text to encode: ", strip=False)
        encoded = base64.b64encode(text.encode("utf-8")).decode("ascii")
        print(f"\n  Encoded: {encoded}")
    else:
        encoded = ask("Base64 text to decode: ")
        try:
            decoded = base64.b64decode(encoded.encode("ascii"), validate=True).decode("utf-8")
            print(f"\n  Decoded: {decoded}")
        except (ValueError, UnicodeError) as exc:
            print(f"  That isn't valid Base64 text: {exc}")


def password_generator():
    heading("PASSWORD GENERATOR")
    length = ask_int("Password length (8–64): ", 8, 64)
    use_symbols = ask_yes_no("Include symbols? (y/n): ", default=True)
    pool = string.ascii_letters + string.digits + ("!@#$%^&*()-_=+[]{}?" if use_symbols else "")
    required = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase), secrets.choice(string.digits)]
    if use_symbols:
        required.append(secrets.choice("!@#$%^&*()-_=+[]{}?"))
    password = required + [secrets.choice(pool) for _ in range(length - len(required))]
    password = "".join(secrets.SystemRandom().sample(password, len(password)))
    print(f"\n  Your password: {password}")
    print("  It has not been saved to a file.")


def notes_pad():
    heading("MINI NOTEPAD")
    path = data_path("notes.txt")
    print("1. View notes   2. Add a note   3. Clear notes")
    choice = ask_choice("Choose: ", {
        "1": ["view", "read", "show notes", "1"],
        "2": ["add", "write", "new note", "save note", "2"],
        "3": ["clear", "delete all", "wipe notes", "3"],
    }, retry_message="Try view, add, or clear.")
    if choice == "1":
        if not os.path.exists(path):
            print("  Your notebook is empty.")
        else:
            with open(path, "r", encoding="utf-8") as file:
                notes = file.read()
            if not notes.strip():
                print("  Your notebook is empty.")
            else:
                print("\n" + "─" * 64)
                print(notes, end="" if notes.endswith("\n") else "\n")
                print("─" * 64)
    elif choice == "2":
        note = ask("Write one note: ", strip=False)
        if not note.strip():
            print("  Empty notes were not saved.")
            return
        with open(path, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("  Note saved locally in data/notes.txt")
    elif choice == "3":
        confirm = ask_yes_no("Clear all notes permanently? (y/n): ", default=False)
        if confirm:
            open(path, "w", encoding="utf-8").close()
            print("  Notes cleared.")
        else:
            print("  Cancelled; nothing changed.")
    else:
        print("  Choose 1, 2, or 3.")


def todo_manager():
    import json
    path = data_path("todo.json")

    def load_tasks():
        try:
            with open(path, "r", encoding="utf-8") as file:
                value = json.load(file)
            if not isinstance(value, list):
                return []
            return [task for task in value if isinstance(task, dict) and isinstance(task.get("text", ""), str)]
        except (OSError, json.JSONDecodeError):
            return []

    def save_tasks(tasks):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

    heading("TO-DO QUEST MANAGER")
    tasks = load_tasks()
    print("1. View tasks   2. Add task   3. Mark done   4. Delete task")
    choice = ask_choice("Choose: ", {
        "1": ["view", "list", "show tasks", "1"],
        "2": ["add", "new task", "create task", "2"],
        "3": ["done", "complete", "mark done", "finish task", "3"],
        "4": ["delete", "remove", "remove task", "4"],
    }, retry_message="Try view, add, done, or delete.")
    if choice == "1":
        if not tasks:
            print("  Nothing on your quest list. Add a task to get started!")
        for i, task in enumerate(tasks, 1):
            mark = "✓" if task.get("done") else " "
            print(f"  {i:02}. [{mark}] {task.get('text', '(empty task)')}")
    elif choice == "2":
        task = ask("New task: ")
        if task:
            tasks.append({"text": task, "done": False})
            save_tasks(tasks)
            print("  Quest added! Saved locally.")
        else:
            print("  Empty task not added.")
    elif choice in ("3", "4"):
        if not tasks:
            print("  Your task list is empty.")
            return
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {'✓' if task.get('done') else ' '} {task.get('text', '')}")
        index = ask_int("Task number: ", 1, len(tasks)) - 1
        if choice == "3":
            tasks[index]["done"] = not tasks[index].get("done", False)
            print("  Task marked done." if tasks[index]["done"] else "  Task marked not done.")
        else:
            removed = tasks.pop(index)
            print(f"  Deleted: {removed.get('text', '')}")
        save_tasks(tasks)
    else:
        print("  Choose 1, 2, 3, or 4.")


def open_website():
    heading("WEBSITE LAUNCHER")
    raw = ask("Website (example: youtube.com): ")
    if not raw:
        print("  Enter a website address first.")
        return
    if "//" not in raw:
        raw = "https://" + raw
    parsed = urlparse(raw)
    if parsed.scheme not in ("http", "https") or not parsed.hostname or "." not in parsed.hostname:
        print("  That address doesn't look valid. Try something like example.com")
        return
    try:
        print("  Browser launch requested." if webbrowser.open(raw) else "  The browser did not confirm opening the page.")
    except Exception as exc:
        print(f"  Could not open the browser: {exc}")


def stopwatch():
    heading("STOPWATCH")
    print("The clock starts now. Press Enter when you want to stop it.")
    started = time.monotonic()
    ask("GO! Press Enter to stop... ")
    elapsed = time.monotonic() - started
    minutes, seconds = divmod(elapsed, 60)
    print(f"\n  ⏱ {int(minutes):02}:{seconds:05.2f}")


def countdown_timer():
    heading("COUNTDOWN TIMER")
    seconds = ask_int("Countdown seconds (1–300): ", 1, 300)
    print("  Timer started. Press Ctrl+C to stop it early.")
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"\r  Remaining: {mins:02}:{secs:02}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print("\r  ⏰ TIME'S UP!" + " " * 20)
        try:
            print("\a", end="")
        except Exception:
            pass
    except KeyboardInterrupt:
        print("\n  Timer stopped early.")
