import random, string


def string(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))
