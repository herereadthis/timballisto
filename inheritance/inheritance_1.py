"""Demo inheritance."""

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        """Explicitly invoke the __init__ method of the Person superclass."""
        # Meh
        # Person.__init__(self, first, last)
        # Better
        super().__init__(self, first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber


if __name__ == '__main__':
    x = Person("Marge", "Simpson")
    y = Employee("Homer", "Simpson", "1007")

    print(x.Name())
    print(y.GetEmployee())
