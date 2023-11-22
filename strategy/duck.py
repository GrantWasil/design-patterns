from fly_behavior import *
from quack_behavior import *

class Duck: 
    def __init__(self):
        self._fly_behavior = FlyBehavior()
        self._quack_behavior = QuackBehavior()
    
    def display(self):
        raise NotImplementedError
    
    def setFlyBehavior(self, fb):
        self._fly_behavior = fb

    def setQuackBehavior(self, qb):
        self._quack_behavior = qb
    
    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyWithWings()
        self._quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyNoWay()
        self._quack_behavior = Quack()
    
    def display(self):
        print("I'm a model duck")


mallard = MallardDuck()
mallard.display()
mallard.perform_quack()
mallard.perform_fly()

model = ModelDuck()
model.display()
model.perform_fly()
model.setFlyBehavior(FlyRocketPowered())
model.perform_fly()