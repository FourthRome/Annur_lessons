if __name__ == "__main__":
    # 1. Ошибки компиляции, в частности, ошибки парсинга (parse) 
    # 2. Ошибки времени выполнения (runtime errors)
    # 3. Продуктовые ошибки

    # arr = [0, 1]
    # for j in range(5):
    #     for i in range(3):
    #         print(j)
    #         print(arr[i])

    # Механизм исключений (exceptions)
    def raise_error():
        # 10 / 0
        # 2 + "2"
        # a = []
        # a[2]
        raise Exception
    
    def handle_exception():
        raise_error()
        print("That was not supposed to be printed")
    
    # try-catch
    # try-except
    # try:
    #     handle_exception()
    # except ZeroDivisionError:
    #     print("Handled safely!")
    # except TypeError:
    #     print("Handled safely again!")
    # except Exception as e:
    #     print("Handled grandpa of all exceptions! ", type(e))
    # # except:
    # #     print("What are you?")
    # finally:
    #     print("Yeah, finally")

    # if type(handle_exception()) == ZeroDivisionError:
    #     print("Another way to handle errors?..")

    # break_flag = False
    # while not break_flag:
    #     inp = input()
    #     is_number = True
    #     for char in inp:
    #         if char not in {'0','1','2','3','4','5'}:
    #             print("Not a number!")
    #             is_number = False
    #             break
    #     if is_number:
    #         b = int(inp)
    #         print(f"Got number {b}")
    #         break_flag = True

    # Easier to ask forgiveness
    break_flag = False
    while not break_flag:
        inp = input()
        try:
            b = int(inp)
            break_flag = True
        except Exception as e:
            print(f"Not a number; error: {e}")
