class Jarmu:
    def diesel(self):
        print("Ez a jármű Dieseles!")
    def benzin(self):
        print("Ez a jármű Benzines!")
    def hibrid(self):
        print("Ez a jármű Hibrid!")
    def elektromos(self):
        print("Ez a jármű Elektromos!")
    
class Auto(Jarmu):
    def __init__(self, ajto:int, kerekek:int, marka:str, toltes:str):
        self.ajto       = ajto
        self.kerekek    = kerekek
        self.marka      = marka
        self.toltes     = toltes

mustang_gt = Auto(2, 4, "Ford", "B")
fiesta = Auto(4, 4, "Ford", "D")
urus = Auto(4, 4, "Lamborghini", "H")
f10 = Auto(2, 4, "Ferrari", "E")
