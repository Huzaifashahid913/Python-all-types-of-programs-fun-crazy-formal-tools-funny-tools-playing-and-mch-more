
import random
def play():
    def main():
        def word():
            tt = input("""Enter word, if you are giving multiple so end it with ".": """)
            if tt == "exit":
                exit()
            global var
            var = tt
            if (tt.endswith(".")):
                tt = tt.split()
                for i in tt:
                    ls = ["p8.", "}?z", "thC", "$@H", "Z^=", "?4l", "T$8", "sX2", "O*d", "@=F", "*jN", "e$d", "zX+", "@G8", "n49", "[d5", "1}w", "@Xq", "9+^", "cuK", "1;w", "$y(", "7:B", ",Z8", "!7F", ",Dm""OyW", "]?t", "hZE", "_);"]
                    ps = ["^", "2", "h", "X", "8", "$", "F", "t", "/", "*"]
                    we = random.choice(ls)
                    me = random.choice(ps)
                    th = i[:1]
                    i = i[1:]
                    just = f"{we}{i}{me}{th}{we}"
                    print(just, end=" ")
            else:
                ls = ["p8.", "}?z", "thC", "$@H", "Z^=", "?4l", "T$8", "sX2", "O*d", "@=F", "*jN", "e$d", "zX+", "@G8", "n49", "[d5", "1}w", "@Xq", "9+^", "cuK", "1;w", "$y(", "7:B", ",Z8", "!7F", ",Dm""OyW", "]?t", "hZE", "_);"]
                ps = ["^", "2", "h", "X", "8", "$", "F", "t", "/", "*"]
                we = random.choice(ls)
                me = random.choice(ps)
                th = tt[:1]
                tt = tt[1:]
                just = f"{we}{tt}{me}{th}{we}"
                print(just)
                return just

        encoded_word = word()
        now = input("\nnow tell me what to do: ")
        if now == "exit":
            exit()
        while now != "decode" and now != "more":
            print("Please enter correct")
            now = input("now please enter correct: ")
            if now == "exit":
                exit()

        if now == "decode":
            print(var)

        elif now == "more":
            word()
    while True:
        main()

if __name__ == "__main__":
    play()