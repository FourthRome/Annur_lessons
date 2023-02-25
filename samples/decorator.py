def func(fun):
    def wrapper(n):
        print("hello")
        fun(n)
        print("world")
    return wrapper


#@func
def some_func(n):
    print(n, n - 1, n -2)


if __name__ == "__main__":
    (func(some_func))(3)


def my_test():
    # business logic
    pass
