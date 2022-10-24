import memory

if __name__ == "__main__":
    print(a)
    a = {"a", "b", "c"}
    for value in a:
        print(value)

    if "a" in a:
        print("YEss")
    a.add("d")
    
    b = {"hello": "world", "a": "b"}

    for key, value in b.items():
        print(key, value)

