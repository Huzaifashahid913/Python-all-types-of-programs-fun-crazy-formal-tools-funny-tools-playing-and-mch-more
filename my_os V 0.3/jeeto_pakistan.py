from games import jeeto_pakistan
from common import BackToMenu


def play():
    try:
        jeeto_pakistan()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
