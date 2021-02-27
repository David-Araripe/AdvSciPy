class Person:

    def __init__(self, firstn, lastn, *args):
        self.firstname = firstn
        self.lastname = lastn

    def printName(self):
        print(self.firstname + self.lastname)

class Student(Person):
    
    def __init__(self, firstn, lastn, arg):
        super().__init__(firstn, lastn, arg)
        self.study = arg
    
    def printNameSubject(self):
        print(self.firstname, self.lastname + ",", self.study)

class Teacher(Person):

    def __init__(self, firstn, lastn, arg):
        super().__init__(firstn, lastn, arg)
        self.teaches = arg

    def printNameSubject(self):
        print(self.firstname, self.lastname + ",", self.teaches)



