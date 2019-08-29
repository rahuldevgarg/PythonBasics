a = list(map(int, input("Enter space separated values : ").split()))


def trueFalse(a):
    if a == 0:
        return None
    elif a % 2 == 0:
        return True
    else:
        return False


h = list(map(trueFalse, a))
print(h)
