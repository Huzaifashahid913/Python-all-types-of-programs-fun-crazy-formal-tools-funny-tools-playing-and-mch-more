import difflib
import os
import re


class BackToMenu(Exception):
    """Leave the current app and return to the main menu."""


def normalize(value):
    value = value.casefold().strip()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def ask(prompt="Your choice: ", strip=True):
    try:
        raw = input(prompt)
    except (EOFError, KeyboardInterrupt):
        raise BackToMenu
    if normalize(raw) in {"exit", "quit", "back", "menu", "return", "go back"}:
        raise BackToMenu
    return raw.strip() if strip else raw


def match_alias(raw, options):
    """Return the canonical option for a forgiving name/shortcut match.

    options is {canonical_name: [aliases...]}. Matches punctuation/case differences,
    harmless extra words, and common small typos without using eval or executing input.
    """
    query = normalize(raw)
    if not query:
        return None
    choices = []
    for canonical, aliases in options.items():
        all_names = [canonical, *aliases]
        for alias in all_names:
            normalized = normalize(alias)
            if normalized:
                choices.append((normalized, canonical))
    # Exact matches always win.
    for alias, canonical in choices:
        if query == alias:
            return canonical
    # If the user says something like "please open calculator", use the longest clear match.
    embedded = [(len(alias), canonical) for alias, canonical in choices
                if len(alias) >= 4 and (f" {alias} " in f" {query} " or query.endswith(alias))]
    if embedded:
        return max(embedded)[1]
    # Let single short phrases like "play game" resolve to a unique alias.
    query_words = set(query.split())
    word_matches = []
    for alias, canonical in choices:
        alias_words = set(alias.split())
        if len(alias_words) == 1 and len(alias) >= 4 and alias in query_words:
            word_matches.append((len(alias), canonical))
    if word_matches:
        return max(word_matches)[1]
    # Typo tolerance is conservative; never fuzzy-match one- or two-character input.
    if len(query) >= 4:
        aliases = list(dict.fromkeys(alias for alias, _ in choices if len(alias) >= 4))
        close = difflib.get_close_matches(query, aliases, n=1, cutoff=0.72)
        if close:
            return next(canonical for alias, canonical in choices if alias == close[0])
    return None


def ask_choice(prompt, options, *, retry_message="Choose one of the listed options."):
    while True:
        raw = ask(prompt)
        result = match_alias(raw, options)
        if result is not None:
            return result
        print(f"  {retry_message}")


def ask_int(prompt, minimum=None, maximum=None):
    while True:
        value = ask(prompt)
        try:
            number = int(value)
        except (TypeError, ValueError, OverflowError):
            print("  Please enter a whole number, like 12.")
            continue
        if minimum is not None and number < minimum:
            print(f"  Please enter {minimum} or higher.")
            continue
        if maximum is not None and number > maximum:
            print(f"  Please enter {maximum} or lower.")
            continue
        return number


def ask_float(prompt, minimum=None, maximum=None):
    while True:
        value = ask(prompt)
        try:
            number = float(value)
            if number != number or number in (float("inf"), float("-inf")):
                raise ValueError
        except (TypeError, ValueError, OverflowError):
            print("  Please enter a normal number, like 12.5.")
            continue
        if minimum is not None and number < minimum:
            print(f"  Please enter {minimum} or higher.")
            continue
        if maximum is not None and number > maximum:
            print(f"  Please enter {maximum} or lower.")
            continue
        return number


def ask_yes_no(prompt, default=None):
    options = {"yes": ["y", "yeah", "yep", "sure", "ok", "okay", "true", "1", "please do"],
               "no": ["n", "nope", "nah", "false", "0", "dont", "don't"]}
    while True:
        raw = ask(prompt)
        result = match_alias(raw, options)
        if result:
            return result == "yes"
        if raw.strip() == "" and default is not None:
            return default
        print("  Please answer yes or no (y/n).")


def heading(title):
    title = f" {title.strip().upper()} "
    width = 52
    if len(title) > width - 2:
        title = title[:width - 2]
    print("\n╭" + "─" * (width - 2) + "╮")
    print("│" + title.center(width - 2) + "│")
    print("╰" + "─" * (width - 2) + "╯")


def line(char="─", width=52):
    print("  " + char * width)


def data_path(filename):
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, filename)


def pause(message="Press Enter to return to MyOS..."):
    try:
        input(message)
    except (EOFError, KeyboardInterrupt):
        pass
