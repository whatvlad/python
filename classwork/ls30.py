class Car:
    def __init__(self, marka, model, year, addometr):
        self.marka = marka
        self.model = model
        self.year = year
        self.addometr = 0

    def get_descrypt_name(self):
        print(f"Marka mashini: {self.marka}, model mashini: {self.model}, god vihoda: {self.year}")

    def read_addometr(self):
        print(f"Addometr: {self.addometr}")

    def update_addometr(self, n):
        if n >= self.addometr:
            self.addometr = n
        else:
            print("Изменить нельзя")

    def increment_addometr(self, m):
        self.addometr += m
        print(f"Probeg: {self.addometr}")


myNewCar = Car("BMW", "X10", 2025, 0)
myNewCar.get_descrypt_name()
myNewCar.addometr = 23
n = int(input("Vvedite addometr: "))
m = int(input("Miles: "))
myNewCar.update_addometr(n)
myNewCar.read_addometr()
myNewCar.increment_addometr(m)


class Electrocar(Car):

    def __init__(self, marka, model, year, addometr, battery):
        Car.__init__(self, marka, model, year, battery)
        self.battery = battery

    def name_electrocar(self):
        print(f"Marka mashini: {self.marka}, model mashini: {self.model}, god vihoda: {self.year}, battery: {self.battery}")

    def new_battery(self, b):
        print(f"Vasha battery: {b}")


b = int(input("Vvedite batareyu: "))
ecar = Electrocar("Tesla", "Tesla Model X", 2017, 0, b)
ecar.name_electrocar()
ecar.new_battery(b)







