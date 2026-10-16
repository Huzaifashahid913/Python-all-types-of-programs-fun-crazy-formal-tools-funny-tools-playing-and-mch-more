from tools import secret_text
from common import BackToMenu


def play():
    try:
        secret_text()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
