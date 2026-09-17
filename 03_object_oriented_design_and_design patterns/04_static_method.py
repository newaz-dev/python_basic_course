class Cha:
    cha_name = "Ada Cha"

    @staticmethod
    def sell_cha(money):
        if money == 10:
            return "One cup cha"
        else:
            return "please 10 taka den, tahole ek cup cha dibo"
print(Cha.sell_cha(10))

#Eta kindoff independent helper functionn, 
#jokhon dorkar hoy name dhore call kori thats it.