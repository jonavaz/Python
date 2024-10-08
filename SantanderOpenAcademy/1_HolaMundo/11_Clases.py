### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    # Constructor de clase
    def __init__(self, name, surname, alias = "Sin alias"):
        # Atributos/Propiedades públicas
        self.full_name = f"{name} {surname} ({alias})"
        # Atributos/Propiedades privados
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminado...")
    

my_person = Person("Jonathan", "Vázquez")
print(my_person.get_name())
my_person.walk()


my_other_person = Person("Jonathan", "Vázquez", "Jona")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Ponce de León (El Loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 66
print(my_other_person.full_name)