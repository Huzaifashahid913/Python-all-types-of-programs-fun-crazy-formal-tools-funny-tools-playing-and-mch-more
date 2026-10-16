import webbrowser
import breaking_news
import create_secret_word
import joke_teller
import jeeto_pakistan
import reverse_table_creator
import snake_water_gun_game
import star_piramids

def play(): 
    want = input("What you want todo bro(games/news/joke/open_website): ").lower()

    if want == "joke":
        joke_teller.play()
    elif want == "games" or want == "game" or want == "play" or "game" in want:
        print("\nThere are many games\ncreate_secret_word(csw): In this your entered word will codded and decodded,\njeeto_pakistan(jp): In this we'll answer our questions and earn money\nreverse_table_creator(rtc): In this you can create table of any number reverse,\nsnake_water_gun(swg): in this you can play snake water gun game,\nstar_piramids(sp): in this your entered value would be converted into a piramid made by stars,\nfor playing write exact name or short name given in the paranthases,\n")
        want = input("Which game you want to play: ").lower()
        if want == "csw" or want == "create_secret_word":
            create_secret_word.play()
        elif want == "jeeto_pakistan" or want == "jp":
            jeeto_pakistan.play()
        elif want == "reverse_table_creator" or want == "rtc":
            reverse_table_creator.play()
        elif want == "snake_water_gun" or want == "swg":
            snake_water_gun_game.play()
        elif want == "star_piramids" or want == "sp":
            star_piramids.play()
        else:
            print("It looks like you didn't entered correct, please try again")
    elif want == "news":
        breaking_news.play()
    elif want == "website" or want == "open_website" or "website" in want:
        choice = input("Which website you want to open enter like youtube.com, google.com: ")
        if "." in choice or ".com" in choice or ".net" in choice or ".org" in choice or ".ai" in choice:
            webbrowser.open(f"https://www.{choice}")
        else:
            print("I think you didn't entered right way")
    else:
        print("It looks you didn't entered correct thing, please try again")

while True:
    if __name__ == "__main__":
        play()