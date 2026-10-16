HUZAIFA MyOS — Python Playground
================================

START
-----
1. Extract this ZIP.
2. Double-click run.bat on Windows.
3. Type an app name/number, or start with: games, fun, tools, online, time.

The first menu is intentionally short to fit a small screen. Type list to view
all 25 apps. Menu names accept common aliases and small typos (e.g. calc,
calcluator, games, game). At a prompt, type exit/back/menu to return to MyOS.
Type exit at the main menu to close it.

THE 25 APPS
-----------
 1 Guess the Number           14 Reverse Multiplication Table
 2 Snake Water Gun            15 Star Pattern Studio
 3 Tic-Tac-Toe                16 Unit Converter
 4 Word Scramble              17 Text Analyzer
 5 Hangman                    18 Secret Text Encoder/Decoder
 6 Math Sprint                19 Password Generator
 7 Jeeto Pakistan Quiz        20 Mini Notepad
 8 Magic 8-Ball               21 To-Do Quest Manager
 9 Dice Roller                22 Breaking News Search
10 Coin Toss                  23 Website Launcher
11 Random Picker              24 Stopwatch
12 Joke Teller                25 Countdown Timer
13 Smart Calculator

PACKAGES
--------
No packages are required for the core program. It uses Python's standard
library. Optional voice support for Joke Teller uses pyttsx3.
Install it with: python -m pip install -r requirements.txt
Or double-click install_optional.bat.

FILES / INTERNET
----------------
Notes and tasks save locally under data/. Breaking News needs an internet
connection and uses a public Google News RSS feed. Website Launcher opens a
site in your browser. News and website availability depend on external services.

IMPORTANT
---------
- This is a terminal-based Python playground, not a replacement for Windows.
- Base64 is encoding, not encryption; do not use it to secure secrets.
- Jeeto Pakistan's prize is fictional; no real money is awarded.
- The calculator accepts basic arithmetic, not Python code execution.

TEST
----
Open a terminal in this folder and run: python -m unittest -v
