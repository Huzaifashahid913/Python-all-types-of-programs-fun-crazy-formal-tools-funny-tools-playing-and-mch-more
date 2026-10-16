classes = {
    "class1" : ["Zaib", "Huzaifa", "Samad", "Shahid", "Amir"],
    "class2" : ["Shnahid", "Amir"],
    "class3" : ["Aqib", "Sameer", "Ali"],
    "class4" : ["Zaib", "Huzaifa", "Samad", "Shahid", "Amir"],
    "class5" : ["Shahid", "Amir"],
    "class6" : ["Aqib", "Sameer", "Ali"]
}

user_choice = input("Which class you want to see: ")
if user_choice in classes:
    pass
else:
    print("Sorry you can't do that, This class is not available")
    exit()
use_choice = classes.get(user_choice)

class students:
    def __init__(self, grade):
        self.grade = grade
        if (len(grade) >= 5):
            print("This class needs a Teacher")
        for name in grade:
            print(name)
        print(f"There are {len(grade)} studetns in this class")

students(use_choice)