import os
from common import BackToMenu, heading, match_alias
import games
import tools
import breaking_news


APPS = [
    ("Guess the Number", "Game", games.guess_the_number, ("guess", "number guess", "gtn", "guessing game")),
    ("Snake Water Gun", "Game", games.snake_water_gun, ("snake", "water gun", "swg", "rock paper scissors style")),
    ("Tic-Tac-Toe", "Game", games.tic_tac_toe, ("tic tac toe", "tictactoe", "ttt", "xo", "crosses and noughts")),
    ("Word Scramble", "Game", games.word_scramble, ("scramble", "scrambled words", "word jumble")),
    ("Hangman", "Game", games.hangman, ("hangman", "hang", "guess the word")),
    ("Math Sprint", "Game", games.math_sprint, ("math", "math quiz", "mental maths", "maths sprint")),
    ("Jeeto Pakistan Quiz", "Game", games.jeeto_pakistan, ("jeeto", "jp", "quiz", "trivia", "general knowledge")),
    ("Magic 8-Ball", "Fun", games.magic_8_ball, ("magic", "8 ball", "eight ball", "fortune ball", "predict")),
    ("Dice Roller", "Fun", games.dice_roller, ("dice", "roll dice", "roll a die")),
    ("Coin Toss", "Fun", games.coin_toss, ("coin", "flip coin", "heads or tails", "coin flip")),
    ("Random Picker", "Fun", games.random_picker, ("picker", "choose for me", "decision", "random choice", "pick one")),
    ("Joke Teller", "Fun", games.joke_teller, ("joke", "jokes", "funny", "make me laugh")),
    ("Smart Calculator", "Tool", tools.calculator, ("calculator", "calc", "math calculator", "solve")),
    ("Reverse Multiplication Table", "Tool", tools.reverse_table_creator, ("table", "reverse table", "rtc", "multiplication table", "times table")),
    ("Star Pattern Studio", "Tool", tools.star_pyramids, ("stars", "pyramid", "patterns", "sp", "star art", "ascii art")),
    ("Unit Converter", "Tool", tools.unit_converter, ("convert", "units", "converter", "temperature converter")),
    ("Text Analyzer", "Tool", tools.text_analyzer, ("text", "analyze", "analyser", "text stats", "word count")),
    ("Secret Text Encoder / Decoder", "Tool", tools.secret_text, ("secret", "encode", "decode", "csw", "base64", "secret text")),
    ("Password Generator", "Tool", tools.password_generator, ("password", "passgen", "secure password", "make password")),
    ("Mini Notepad", "Tool", tools.notes_pad, ("notes", "notepad", "note pad", "my notes")),
    ("To-Do Quest Manager", "Tool", tools.todo_manager, ("todo", "to do", "to-do", "tasks", "task list", "quest")),
    ("Breaking News Search", "Internet", breaking_news.play, ("news", "breaking news", "headlines", "latest news")),
    ("Website Launcher", "Internet", tools.open_website, ("website", "browser", "open website", "open site", "web", "internet")),
    ("Stopwatch", "Time", tools.stopwatch, ("stop watch", "timer stopwatch", "time counter", "stop time")),
    ("Countdown Timer", "Time", tools.countdown_timer, ("timer", "countdown", "count down", "alarm timer")),
]

CATEGORIES = {
    "Game": ["game", "games", "play", "playing", "gaming", "gem", "gam", "gams"],
    "Fun": ["fun", "funny", "random fun", "entertainment", "fun tools", "funny games", "funny things"],
    "Tool": ["tool", "tools", "utilities", "utility", "useful tools", "apps", "mytools"],
    "Internet": ["internet", "online", "web tools", "web", "open site", "site", "webstie"],
    "Time": ["time", "clock", "time tools", "timers"],
}

MENU_OPTIONS = {
    "list": ["apps", "all apps", "show all", "menu list", "full menu", "show list"],
    "help": ["?", "commands", "how to use", "instructions", "help", "how", "help me", "show help"],
    "clear": ["cls", "clear screen", "clean screen", "clear", "clean", "blank screen", "clear chat"],
    "exit": ["quit", "close", "shutdown", "bye", "goodbye", "stop myos", "exot", "exir"],
}


def compact_menu():
    print("\n╭────────────── HUZAIFA MyOS ──────────────╮")
    print("│ 25 mini apps • Games, fun & useful tools │")
    print("╰──────────────────────────────────────────╯")
    print("Type a number, app name, shortcut, or category:")
    print("  game  •  fun  •  tools  •  online  •  time")
    print("Try: guess, ttt, joke, calc, password, news")
    print("Commands: list = all apps | help | exit")


def show_apps(category=None):
    group = [app for app in APPS if category is None or app[1] == category]
    title = "ALL 25 APPS" if category is None else category.upper() + " APPS"
    heading(title)
    for index, (name, cat, _function, _aliases) in enumerate(group, 1):
        print(f" {index:02}. {name} [{cat.lower()}]")
    print("\nTip: type the app name or its shortcut. Type exit to go back.")


def app_options():
    return {name: list(aliases) for name, _category, _function, aliases in APPS}


def find_app(raw):
    canonical = match_alias(raw, app_options())
    if canonical:
        return next((i for i, app in enumerate(APPS) if app[0] == canonical), None)
    # Short names and phrase-like commands: "play some hangman", "open calc please".
    cleaned = raw.casefold().strip()
    for i, (name, _category, _function, aliases) in enumerate(APPS):
        names = [name.casefold(), *aliases]
        for alias in sorted(names, key=len, reverse=True):
            if len(alias) >= 4 and alias in cleaned:
                return i
    return None

def run_app(index):
    name, _category, function, _aliases = APPS[index]
    print(f"\n▶ {name}")
    try:
        function()
    except BackToMenu:
        print(f"\n  {name} closed. Back to MyOS. 👋")
    except KeyboardInterrupt:
        print(f"\n  {name} stopped. Back to MyOS.")
    except (EOFError, BrokenPipeError):
        print("\n  Input ended. Back to MyOS.")
    except Exception as exc:
        print(f"\n  {name} hit a problem: {exc}")
        print("  MyOS is still open. Try the app again or choose another one.")


def choose_from_category(category):
    show_apps(category)
    while True:
        try:
            raw = input(f"{category} > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBack to MyOS.")
            return
        if raw.casefold().strip() in {"exit", "quit", "back", "menu", "return"}:
            return
        index = find_app(raw)
        if index is not None and APPS[index][1] == category:
            run_app(index)
            return
        if raw.isdigit() and 1 <= int(raw) <= len([a for a in APPS if a[1] == category]):
            category_apps = [i for i, a in enumerate(APPS) if a[1] == category]
            run_app(category_apps[int(raw) - 1])
            return
        category_match = match_alias(raw, CATEGORIES)
        if category_match:
            print("  You're already in that category. Pick an app or type exit.")
        else:
            print("  Didn't catch that. Try an app name/shortcut, or type exit.")


def show_help():
    print("\nHELP: enter 1–25, an app name, or a shortcut (e.g. calc, ttt, gtn).")
    print("Try category words like games/tools/fun to browse a group.")
    print("Inside an app: exit, back, or menu returns here. At MyOS: exit closes it.")


def main():
    while True:
        compact_menu()
        try:
            raw = input("\nMyOS > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nMyOS closed. See you next time! 👋")
            return
        if not raw:
            print("  Type an app name, number, or help.")
            continue
        command = match_alias(raw, MENU_OPTIONS)
        if command == "exit":
            print("\nMyOS closed. See you next time! 👋")
            return
        if command == "help":
            show_help()
            continue
        if command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            continue
        if command == "list":
            show_apps()
            continue
        if raw.isdigit():
            number = int(raw)
            if 1 <= number <= len(APPS):
                run_app(number - 1)
            else:
                print("  Enter an app number from 1 to 25.")
            continue
        # Exact category words open a category; app names take priority in longer phrases.
        category = None
        normalized = raw.casefold().strip()
        for canonical, aliases in CATEGORIES.items():
            if normalized == canonical.casefold() or normalized in [a.casefold() for a in aliases]:
                category = canonical
                break
        if category:
            choose_from_category(category)
            continue
        index = find_app(raw)
        if index is not None:
            run_app(index)
            continue
        # Natural phrases such as "I want to play games" are also supported.
        category = match_alias(raw, CATEGORIES)
        if category is None:
            lower = raw.casefold()
            for canonical, aliases in CATEGORIES.items():
                if any(alias in lower for alias in aliases if len(alias) >= 4):
                    category = canonical
                    break
        if category:
            choose_from_category(category)
        else:
            print("  Not sure what you mean. Try 'games', 'calc', 'guess', 'list', or 'help'.")


if __name__ == "__main__":
    main()
