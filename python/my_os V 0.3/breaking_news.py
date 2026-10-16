import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from common import ask, ask_int, heading


def play():
    heading("BREAKING NEWS SEARCH")
    topic = ask("What news topic do you want? ")
    if not topic:
        print("  Enter a topic to search for.")
        return
    count = ask_int("How many headlines (1–10)? ", 1, 10)
    query = urllib.parse.urlencode({"q": topic, "hl": "en-US", "gl": "US", "ceid": "US:en"})
    url = "https://news.google.com/rss/search?" + query
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 HuzaifaMyOS/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            root = ET.fromstring(response.read())
        stories = root.findall("./channel/item")
        if not stories:
            print("  No headlines found for that search.")
            return
        heading(f"NEWS: {topic[:45]}")
        for i, story in enumerate(stories[:count], 1):
            title = story.findtext("title") or "Untitled"
            link = story.findtext("link") or "No link available"
            source_node = story.find("source")
            source = source_node.text if source_node is not None and source_node.text else "Source unavailable"
            published = story.findtext("pubDate") or "Date unavailable"
            print(f"\n  {i:02}. {title}\n      Source: {source}\n      Published: {published}\n      Read: {link}")
            print("  " + "─" * 60)
    except Exception as exc:
        print("  I couldn't load the news feed. Check your internet and try again.")
        print(f"  Details: {exc}")


if __name__ == "__main__":
    from common import BackToMenu
    try:
        play()
    except BackToMenu:
        print("\nBack to the menu.")
