from games import snake_water_gun
from common import BackToMenu


def play():
    try:
        snake_water_gun()
    except BackToMenu:
        print("\nBack to the menu.")


if __name__ == "__main__":
    play()
