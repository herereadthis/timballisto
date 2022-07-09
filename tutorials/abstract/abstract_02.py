"""Demo Abstract Base Classes."""
# https://docs.python.org/3.6/library/abc.html

from abc import ABC


class MyABC(ABC):
    """Demo this."""

    pass

if __name__ == '__main__':
    MyABC.register(dict)

    my_abc = MyABC()

    print(issubclass(dict, MyABC))
    # >>> True
    print(isinstance({}, MyABC))
    # >>> True

    my_dict = {'a': 'b'}
    my_tuple = ('a', 'b')

    print('\ncheck is instance')
    print(isinstance(my_dict, MyABC))
    # >>> True
    print(isinstance(my_tuple, MyABC))
    # >>> False

    print(MyABC.__class__.__instancecheck__)
    # >>> <function ABCMeta.__instancecheck__ at 0x109646ae8>
    print(MyABC.__class__.__instancecheck__(MyABC, my_dict))
    # >>> True
    print(MyABC.__class__.__instancecheck__(MyABC, {}))
    # >>> True
    print(MyABC.__class__.__instancecheck__(MyABC, my_tuple))
    # >>> False

    print(MyABC._abc_registry.data)
    # >>> {<weakref at 0x10d829688; to 'type' at 0x10d43cdf0 (dict)>}
