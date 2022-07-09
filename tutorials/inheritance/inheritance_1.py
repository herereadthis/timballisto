"""Demo inheritance."""


class Person:
    """Create person."""

    def __init__(self, first, last):
        """initialize."""
        self.firstname = first
        self.lastname = last

    def get_name(self):
        """Get name of person."""
        return '%s %s' % (self.firstname, self.lastname)


class Employee(Person):
    """Create Employee."""

    def __init__(self, first, last, staffnum):
        """Explicitly invoke the __init__ method of the Person superclass."""
        # Meh
        # Person.__init__(self, first, last)
        # Better (python 3 does need arguments)
        super().__init__(first, last)
        # Python2 compatibleL
        # super(Employee, self).__init__(first, last)
        self.staffnumber = staffnum

    def get_employee(self):
        """Get the employee."""
        return '%s, %s' % (self.get_name(), self.staffnumber)


if __name__ == '__main__':
    x = Person("Marge", "Simpson")
    y = Employee("Homer", "Simpson", "1007")

    print(x.get_name())
    print(y.get_employee())
