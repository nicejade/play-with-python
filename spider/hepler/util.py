def print_list(list):
    print("\n".join("{}: {}".format(*k) for k in enumerate(list)))
