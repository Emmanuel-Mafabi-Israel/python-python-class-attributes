# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - INSTANCE METHODS
# BY ISRAEL MAFABI EMMANUEL

approved_breeds:list = [
    "Mastiff", 
    "Chihuahua", 
    "Corgi", 
    "Shar Pei",
    "Beagle", 
    "French Bulldog", 
    "Pug", 
    "Pointer"
]

class Dog:
    def __init__(self, name:str="Sample", breed:str=""):
        self.name  = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, value):
        if value:
            if value in approved_breeds:
                self._breed = value
            else:
                print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

dog = Dog("Miles", "Human")