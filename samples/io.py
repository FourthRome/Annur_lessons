if __name__ == "__main__":
    # a dangerous way
    # file = open("samples/text_input.txt", "r")
    # lines = file.readlines()
    # for line in lines:
    #     print(line.strip())
    # file.close()

    # Old school way
    try:
        file = open("samples/text_input.txt", "r")
        lines = file.readlines()
        file.write("Hi")
        for line in lines:
            print(line.strip())    
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        file.close()

    # The cool way
    with open("samples/text_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    # File opening modes:
    # r - readonly
    # w - write mode (data will be lost)
    # a - append
    # w+ - read & write
