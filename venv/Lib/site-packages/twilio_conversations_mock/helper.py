from string import digits
from random import choice as randomchoice


def create_sid(prefix, size=32):
    random = "".join(randomchoice(digits) for _ in range(size))
    return f"{prefix}{random}"
