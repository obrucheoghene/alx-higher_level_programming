def safe_print_list(my_list=[], x=0):
    """
    a function that prints x elements of a list.
    """
    try:
        len = 0
        for i in range(0, x):
            print(my_list[i], end="")
            len += 1
        print("")
    except:
        pass
    finally:
        return len
