

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

myCar = Car('Kitt', 180)
myCar.talk('Michael')

myOtherCar = Car('Speedy', 55)
myOtherCar.start()



class Race:
    def __init__(self, name, driver_limit) -> None:
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if driver.number_of_drivers <= self.driver_limit:
            self.drivers.append(driver)
        else:
            print("Can't add the driver. The race is full.")

    def get_average_ranking(self):
        total_of_ranks = 0
        number_of_drivers = len(self.drivers)
        if number_of_drivers == 0:
            return 0
        for driver in self.drivers:
            total_of_ranks += driver.get_ranking()
        return total_of_ranks / number_of_drivers

my_race = Race('Seattle 500', 4)
print(my_race.name, my_race.driver_limit, my_race.drivers)



class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking) -> None:
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking


lewis = Driver("Lewis Hamilton", 36, 83)
eliud = Driver("Eliud Kipchoge", 36, 95)
seb = Driver("Sebastian Vettel", 34, 76)
ayrton = Driver("Ayrton Senna", 34, 99)

my_race.add_driver(lewis)
my_race.add_driver(eliud)
my_race.add_driver(seb)
my_race.add_driver(ayrton)

print(my_race.get_average_ranking())
print(ayrton.number_of_drivers)

test = Driver("Testy McTester", 33, 21)

my_race.add_driver(test)