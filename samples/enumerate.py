if __name__ == "__main__":
    arr = ['a', 'b', 'c']

    # Способ 1
    for i in range(len(arr)):
        print(i)
        print(arr[i])
    
    # Способ 2
    i = 0
    for elem in arr:
        print(i)
        print(elem)
        i += 1
    
    # Способ 3
    for i, elem in enumerate(arr):
        print(i)
        print(elem)
