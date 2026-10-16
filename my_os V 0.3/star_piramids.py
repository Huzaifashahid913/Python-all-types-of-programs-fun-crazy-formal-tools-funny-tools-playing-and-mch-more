from tools import star_pyramids
from common import BackToMenu


def play():
    try:
        star_pyramids()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
