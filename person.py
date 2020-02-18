# create a class called Person
class Person:
    # initialise class
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests
        
    # create a hello function for class Person
    def hello(self):
        return "Hello, my name is {} and I am {} years old. My interests are {}".format(self.name, self.age, self.interests)
    
# Instantiate person
person = Person("Ryan", 30, "male", "being a hardarse, agile, and ssd hard drives.")

#print(Person.hello(person))
print(person)
