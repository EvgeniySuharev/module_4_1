from math import inf


def divide(first, second):
    div = 0
    if second == 0:
        div = inf
    else:
        div = first / second
    return div

