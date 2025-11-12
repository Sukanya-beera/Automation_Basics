""" Create a class called Person
It should have an __init__() method with name and age as parameters.
Inside __init__(), store them in self.name and self.age.
Create a display() method that prints the person’s details.
Then write a main() function to create one person object and call the display() method. """

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'{self.name},{self.age}')

if __name__=="__main__":

        p=Person("siri", 22)
        p.display()






