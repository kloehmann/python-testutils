import random, string


def random_string(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))
