def func(list_to_modify):
    list_to_modify.append(10)
    # list_to_modify = []  #- не сделает список пустым
    list_to_modify[:] = []

def dangerous_default(list_to_modify=[]):
    list_to_modify.append(42)
    return list_to_modify

if __name__ == "__main__":
    # a = 5
    # a = 2.3
    # a = "Hello world"
    # a = []
    # func(a)
    # print(a)

    b = [10, 20]
    # print(dangerous_default(b))
    # print(dangerous_default(b))

    print(dangerous_default())
    print(dangerous_default())
    print(dangerous_default(b))
    print(dangerous_default())
