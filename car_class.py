class Car:
    def __init__(self, year_model, make,):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        
    def get_speed(self):
        return self.__speed

the_car = Car(2020, "Mitsubishi")

print("\n------------------------------------------------------------------------")

print("\n\033[33mThe car is starting....\033[0m")
print("\nCurrent speed:", the_car.get_speed(), "mph\n")

print("\033[32mAccelerating...\033[0m")
for i in range(5):
    the_car.accelerate()
    print("Current speed:", the_car.get_speed())

print("\n\033[31mApplying the brakes...\033[0m")
for i in range(5):
    the_car.brake()
    print("Current speed:", the_car.get_speed())

print("\nFinal speed:", the_car.get_speed(), "mph")
print("\n\033[33mThe car has come to a stop.\033[0m")

print("\n------------------------------------------------------------------------")