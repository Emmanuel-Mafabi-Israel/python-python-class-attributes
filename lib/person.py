# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - CLASS ATTRIBUTES,
# BY ISRAEL MAFABI EMMANUEL

approved_jobs:list = [
    "Admin", 
    "Customer Service", 
    "Human Resources", 
    "ITC", 
    "Production", 
    "Legal", 
    "Finance", 
    "Sales", 
    "General Management", 
    "Research & Development", 
    "Marketing", 
    "Purchasing"
]

class Person:
    def __init__(self, name:str="Emmanuel", job:str=""):
        self.name = name
        self.job  = job

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 < len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)

    # def print_person(self):
    #     print(f"{self.name} is an {self.job}")

person = Person("Emmanuel", job="Admin")
# person.print_person()

# sample_string = "guido van rossum"
# print(sample_string.title())