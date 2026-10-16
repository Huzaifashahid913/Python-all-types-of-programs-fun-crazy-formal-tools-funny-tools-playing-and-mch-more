from tools import reverse_table_creator
from common import BackToMenu


def play():
    try:
        reverse_table_creator()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
