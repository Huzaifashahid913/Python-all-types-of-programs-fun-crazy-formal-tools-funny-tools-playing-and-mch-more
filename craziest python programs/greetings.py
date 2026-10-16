import time
from datetime import datetime, timedelta

hour = (datetime.utcnow() + timedelta(hours=5)).hour

print(hour)

if 0 <= hour < 5:
    print("Good Night Sir!")
elif 5 <= hour < 8:
    print("Good Early Morning Sir!")
elif 8 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 14:
    print("Good Noon Sir!")
elif 14 <= hour < 17:
    print("Good Afternoon Sir!")
elif 17 <= hour < 19:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")