"""Demonstrate public, private, and protected attributes."""

PRIV_STR = 'I am private'
PROT_STR = 'I am protected'
PUBL_STR = 'I am public'


class PrivacyClass():
    """Demonstrate public, private, and protected attributes."""

    def __init__(self, priv=PRIV_STR, prot=PROT_STR, pub=PUBL_STR):
        """Initialize."""
        self.__private_attribute = priv
        self._protected_attribute = prot
        self.public_attribute = pub

if __name__ == '__main__':
    test_instance = PrivacyClass()

    try:
        print(test_instance.public_attribute)
    except AttributeError:
        print('test_instance.public_attribute does not exist')

    try:
        print(test_instance._protected_attribute)
    except AttributeError:
        print('test_instance._protected_attribute does not exist')

    print(test_instance._protected_attribute)
    test_instance._protected_attribute = 'am i protected?'
    print(test_instance._protected_attribute)

    try:
        print(test_instance.__private_attribute)
    except AttributeError:
        print('test_instance.__private_attribute does not exist')
