import pyttsx3
import pyjokes

def play():
    want = input("""What you want to hear "joke" or a "jokes" """)
    if want == "jokes":
        joke = pyjokes.get_jokes()
        engine = pyttsx3.init()
        def speak_word(name, location, length):
            word = joke[location:location + length]
            print(word, end=" ", flush=True)
        engine.connect("started-word", speak_word)
        engine.say(joke)
        engine.runAndWait()
    elif(want == "joke"):
        joke = pyjokes.get_joke()
        engine = pyttsx3.init()
        def speak_word(name, location, length):
            word = joke[location:location + length]
            print(word, end=" ", flush=True)
        engine.connect("started-word", speak_word)
        engine.say(joke)
        engine.runAndWait()
    else:
        print("I think you entered incorrect word")


if __name__ == "__main__":
    play()