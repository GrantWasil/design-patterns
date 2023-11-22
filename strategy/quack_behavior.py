
class QuackBehavior:
    def quack(self):
        raise NotImplementedErrords

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")