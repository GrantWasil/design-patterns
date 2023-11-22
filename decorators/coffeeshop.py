
class Beverage:
    def __init__(self):
        self.description = "Unkown Beverage"

    def getDescription(self):
        return self.description
    
    def cost(self):
        raise NotImplementedError
    

class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "A nice house blend"
    
    def cost(self):
        return 3.50
    
class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "A nice decaf"
    
    def cost(self):
        return 2.75

class Expresso(Beverage):
    def __init__(self):
       super().__init__()
       self.description = "A brutal decaf sucker punch"
    
    def cost(self):
        return 1.50
    

class CondimentDecorator(Beverage):
    def getDescription(self):
        raise NotImplementedError
    

class Whip:
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"
    
    def cost(self):
        return self.beverage.cost() +.10

class Milk:
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"
    
    def cost(self):
        return self.beverage.cost() +.50
    
class Mocha:
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"
    
    def cost(self):
        return self.beverage.cost() +.12
    

houseBlend = HouseBlend()
print(houseBlend.getDescription())
print(houseBlend.cost())

specialOrder = Mocha(Mocha(Whip(Milk(Expresso()))))
print(specialOrder.getDescription())
print(specialOrder.cost())

specialOrder2 = Expresso()
specialOrder2 = Milk(specialOrder2)
specialOrder2 = Whip(specialOrder2)
specialOrder2 = Mocha(specialOrder2)
specialOrder2 = Mocha(specialOrder2)
print(specialOrder2.getDescription())
print(specialOrder2.cost())

