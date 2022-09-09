class Person:
    def __init__(self, in_name, in_age):
        self.name = in_name
        self.age = in_age

    def get_name(self):
        return self.name

from enum import Enum

class Zoo:
    def __init__(self, name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

nycZoo = Zoo("NYC Zoo")


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def make_noise(self):
        print("Every animal makes noise")

    def eat_food(self):
        print("All creatures need sustenance")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print("slurp, whoosh")

    def eat_food(self):
        print("stuff fish eat")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print("tweet, chirp")

    def eat_food(self):
        print("insects, worms, other things")


class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print("oo aa aa")

    def eat_food(self):
        print("stuff chimps eat. vegetables? trees? plants?")


salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

class Ticket_Type(Enum):
    ADULT = 1
    CHILD = 2

class Customer(Person):
    def __init__(self, in_name, in_age):
        super().__init__(in_name, in_age)
        self.has_ticket_for_zoo = False
        self.is_in_the_zoo = False
        self.ticket_type = None

    def buy_ticket(self, ticket_type):
        self.has_ticket_for_zoo = True
        self.ticket_type = ticket_type

    def enter_zoo(self, zoo):
      if self.has_ticket_for_zoo:
          zoo.add_customer(self.name)
          self.is_in_the_zoo = True
          self.has_ticket_for_zoo = False
      else:
        print("You must purchase a ticket to enter the zoo")

    def exit_zoo(self, zoo):
        zoo.remove_customer(self.name)
        self.is_in_the_zoo = False


alice = Customer("Alice", 25)
bob = Customer("Bob", 20)
charlie = Customer("Charlie", 10)
dave = Customer("Dave", 30)
for c in [alice, bob, charlie, dave]:
    c.buy_ticket(Ticket_Type.ADULT)
    c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)
