from math import fmod


def fmod_wrapper(a, b):
    try:
        float(a)
        float(b)
    except ValueError:
        raise TypeError

    if b == 0:
        raise ValueError

    return fmod(a, b)
