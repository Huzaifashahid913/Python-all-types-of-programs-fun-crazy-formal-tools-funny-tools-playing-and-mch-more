import time
import pyttsx3
from plyer import notification
i = 5 

while i<7:
    print("Setting up the reminder...")
    time.sleep(500)
    pr = ("it's time to drink water so far Huzaifa bro")
    engine = pyttsx3.init()
    engine.say(pr)
    engine.runAndWait()
    print(pr)
    notification.notify(
        title="Your Python alert bro",
        message="it's time to drink water so far Huzaifa",
        app_name="Your python",
        timeout=1
    )
    del engine
