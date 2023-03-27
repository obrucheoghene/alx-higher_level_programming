def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for i in range(0, x):
            print(my_list[i], end="")
            len += 1
        print("")
    except IndexError:
        print("")
    finally:
        return len
