"""Demo inheritance, but with overriding."""


class Person:
    """Create person."""

    def __init__(self, first, last, age):
        """initialize."""
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        """Return stringified version of instance (overriding)."""
        return '%s %s, %d' % (self.firstname, self.lastname, self.age)


class Employee(Person):
    """Create Employee."""

    def __init__(self, first, last, age, staffnum):
        """Explicitly invoke the __init__ method of the Person superclass."""
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        """Return stringified version of employee."""
        """
        Method overriding is an object-oriented programming feature that allows
        a subclass to provide a different implementation of a method that is
        already defined by its superclass or by one of its superclasses.
        """
        return '%s, %s' % (super().__str__(), self.staffnumber)

    def get_employee(self):
        """Get the employee."""
        return '%s, %s' % (self.get_name(), self.staffnumber)


if __name__ == '__main__':
    x = Person("Marge", "Simpson", 36)
    y = Employee("Homer", "Simpson", 42, "1007")

    print(x)
    print(y)
