import random, string


def random_string(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))


def random_iterator(length, elem_creator, *args):
    return iter(random_list(length, elem_creator, *args))


def random_list(length, elem_creator, *args):
    return [elem_creator(*args) for i in range(length)]


def random_bool():
    return random.choice((True, False))
