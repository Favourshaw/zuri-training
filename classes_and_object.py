class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print(self.name, " was changed to ", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print(self.age, " was changed to ", change_age)

    def add_track(self, change_track):
        self.change_tracks = change_track
        print(self.tracks, " was changed to ", change_track)

    def get_score(self):
        print("Score remains ", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
