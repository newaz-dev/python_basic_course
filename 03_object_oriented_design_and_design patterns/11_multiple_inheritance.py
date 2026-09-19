class Father:
    def __init__(self, character):
        self.character = character

    def father_output(self):
        print("This is from Father class")


class Mother:
    def __init__(self, kindness):
        self.kindness = kindness

    def mother_output(self):
        print("This is from Mother class")


class I(Father, Mother):  # Multiple inheritance
    def __init__(self, outfit, character, kindness):
        Father.__init__(self, character)
        Mother.__init__(self, kindness)
        self.outfit = outfit


I1 = I("Awesome", "Good", "Very kind")
I1.father_output()
I1.father_output()
print(I1.character)