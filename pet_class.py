class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

my_pet = Pet()

print("\n------------------------------------------------------------------------")

print("\n\033[33mPet Information\033[0m")
name = input("Enter the name of your pet: ")
animal_type = input("Enter the type of your pet (Dog, Cat, Fish, etc.): ")
age = int(input("Enter the age of your pet: "))

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\n------------------------------------------------------------------------")

print("\n\033[34mPet Profile:\033[0m")
print("Name:", my_pet.get_name())
print("Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())

print("\n------------------------------------------------------------------------")
