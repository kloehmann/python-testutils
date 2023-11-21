import random, string, sys


def random_bytes(length: int = 0) -> bytes:
    """random_bytes(length) returns a byte array of given length

    if no length is specified, a random length will be used
    """
    length = length or random_int(1, 1024)
    return random.randbytes(length)


def random_int(min: int = 0, max: int = sys.maxsize):
    """random_int(min, max) - returns a random integer within the given boundaries

    If no boundaries are given, then 0 and sys.maxsize will be used as min and max.
    """
    return random.randint(min, max)


def random_string(length: int = 0):
    """ "random_string(length) - returns a random string

    If no length is provided, a random length between 5 and 30 is used.
    """
    length = length or random_int(5, 30)
    return "".join(random.choice(string.ascii_letters) for i in range(length))


def random_iterator(length, elem_creator, *args):
    """random_iterator(length, elem_creator, *args) returns an iterator with random elements

    elem_creator must be a method that returns an object that implements the iterabel protocol
    *args are the arguments for the elem_creator
    """
    return iter(random_list(length, elem_creator, *args))


def random_list(length, elem_creator, *args):
    """random_list(length, elem_creator, *args) returns a list of random elements

    elem_creator must be a method returning an object
    *args are the arguments to the elem_creator"""
    return [elem_creator(*args) for i in range(length)]


def random_bool():
    """random_bool() returns a random boolean"""
    return random.choice((True, False))
