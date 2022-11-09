def input_output_decorator(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@input_output_decorator
def find_max(*args):
    max = 0
    for arg in args:
        if max < arg:
            max = arg
    return max


print(find_max(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
