
def name_args(**kwargs):
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")


name_args(a=1, b=2)


def all_true(iterable):
    v = True
    for item in iterable:
        v = v and item
    return v


print(all_true([True, True, True]))
print(all_true([True, True, False]))


def one_true(iterable):
    v = False
    for item in iterable:
        v = v or item
    return v


print(one_true([False, False, False]))
print(one_true([False, True, False]))


def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n-1)


print(recursive_factorial(4))


def recursive_deduplicate(s, *args):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s[0]
    if (s[0] and s[1] and s[0] == s[1]):
        return str(s[0]) + recursive_deduplicate(s[2::])
    return str(s[0]) + str(s[1]) + recursive_deduplicate(s[2::])


# def recursive_deduplicate2(s, *args):
#     # if len(s) <= 1 and args[0] and len(args[0] == 0):
#     #     return s
    
    



print(recursive_deduplicate("AABBCC"))
print(recursive_deduplicate("AAACC"))
print(recursive_deduplicate("ABCDEFG"))
