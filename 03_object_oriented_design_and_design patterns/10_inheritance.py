class Grandfather:
    def __init__(self, addiction, fav_drinks):
        self.addiction = addiction
        self.fav_drinks = fav_drinks
class Father(Grandfather):
    def __init__(self, character, addiction, fav_drinks):
        super().__init__(addiction, fav_drinks)
        self.character = character
gf_obj1 = Grandfather("Girls", "Magic Moment")
f_obj1 = Father("Play Boy", "Girls", "Magic Moment")
print(f_obj1.addiction)