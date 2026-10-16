from games import joke_teller
from common import BackToMenu


def play():
    try:
        joke_teller()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
