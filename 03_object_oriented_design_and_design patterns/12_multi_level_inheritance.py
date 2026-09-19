class GrandFather:
    def __init__(self, property, surname):
        self.property = property
        self.surname = surname

    def properties(self):
        print("This is Grandpa's whole property")


class Father(GrandFather):
    def __init__(self, character, property, surname):
        self.character = character
        super().__init__(property, surname)

    def father_output(self):
        print("This is from Father class")


class I(Father):  # Multilevel inheritance
    def __init__(self, outfit, character, property, surname):
        super().__init__(character, property, surname)
        self.outfit = outfit


I1 = I("Awesome", "Good", "Dua", "Newaz")

I1.properties()
I1.father_output()

print(I1.outfit)
print(I1.character)
print(I1.property)
print(I1.surname)