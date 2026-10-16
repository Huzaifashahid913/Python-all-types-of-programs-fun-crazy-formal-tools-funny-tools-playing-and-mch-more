from games import guess_the_number
from common import BackToMenu


def play():
    try:
        guess_the_number()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
