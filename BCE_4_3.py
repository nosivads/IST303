# create Hammer class
class Hammer():
    def used_for(self):
        return "pounds things"

# create Pliers class
class Pliers():
    def used_for(self):
        return "pulls things"

# create Knife class
class Knife():
    def used_for(self):
        return "cuts things"

# create Screwdriver class
class Screwdriver():
    def used_for(self):
        return "screws things"

# create Toolbelt class with instances of Hammer, Pliers, Knife and Screwdriver
# returns a list of actions
class Toolbelt():
    def __init__(self):
        self.hammer = Hammer()
        self.pliers = Pliers()
        self.knife = Knife()
        self.screwdriver = Screwdriver()
    def used_for(self):
        return [tool.used_for() for tool in (self.hammer, self.pliers, self.knife, self.screwdriver)]

# create a Hammer instance, hammer
hammer = Hammer()
print("A hammer", hammer.used_for())

# create a Knife instance, knife
knife = Knife()
print("A knife", knife.used_for())

# create a pliers instance, pliers
pliers = Pliers()
print("A pair of pliers", pliers.used_for())

# create a Screwdriver instance, screwdriver
screwdriver = Screwdriver()
print("A screwdriver", screwdriver.used_for())

# create a Toolbelt instance, toolbelt
# print the actions of the component tools
toolbelt = Toolbelt()
print("A toolbelt contains tools that", ", ".join(toolbelt.used_for()))




