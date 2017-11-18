"""Continue from previous file, use something better than decorators."""


class LittleMeta(type):
    """Create a very simple metaclass."""

    def __new__(cls, clsname, superclasses, attributedict):
        """Do new."""
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class S:
    pass


class A(S, metaclass=LittleMeta):
    pass

if __name__ == '__main__':
    a = A()
