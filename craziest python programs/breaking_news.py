import requests
def play():
    new_type = input("what type of news: ")
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-09-07&sortBy=publishedAt&apiKey=8f8c3041c8534016b794c5a978cd7fe1"

    my = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    data = my.json()

    articles = data["articles"]

    ask = int(input("how much aticles want to read: "))
    print()
    for article in articles[:ask]:

        title = article["title"]
        description = article["description"]
        url = article["url"]

        print("======================================")
        print("TITLE:", title,"\n")
        print("DESCRIPTION:", description,"\n")
        print("READ MORE:", url,"\n")

if __name__ == "__main__":
    play()