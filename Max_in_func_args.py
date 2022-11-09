def find_max(*args):
    max = 0
    for arg in args:
        if max < arg:
            max = arg
    return max

