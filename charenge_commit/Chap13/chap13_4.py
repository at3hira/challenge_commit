class Horse:
    def __init__(self, name, gender, rider):
        self.name = name
        self.gender = gender
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("武豊")
horse_obj = Horse("ディープインパクト", "オス", rider) # composition
print(horse_obj.rider.name)