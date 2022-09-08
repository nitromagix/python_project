
def arb_args(*args):
    for arg in args:
        print(arg)


arb_args("martin", "is", "the", "best")


def inner_func(a, b):
    def nested(c, d):
        return c * d

    return (a / b) + nested(a, b)


print(inner_func(20, 10))


def lunch_lady(name, lunch_preference="Mystery Meat"):
    print(f"{name} - {lunch_preference}")


lunch_lady("Joe", "corn")
lunch_lady("Mary")


def sum_n_product(a, b):
    s = a + b
    p = a * b
    return a, b


print(sum_n_product(3, 7))

alias_arb_args = arb_args

print(alias_arb_args("arbitrary", "args"))


def arb_mean(*args):
    divisor = len(args)
    if divisor == 0:
        return 0
    sum = 0
    for arg in args:
        sum += arg
    return sum / divisor


print(arb_mean(3, 35, 14, 22, 7))
print(arb_mean(13, 6, 10, 4))

def arb_longest_string(*args):
  longest = 0
  for arg in args:
    length = len(arg)
    if length > longest:
      longest = length
  return longest

print(arb_longest_string("an", "mouse", "filibuster", "extraordinary"))
print(arb_longest_string("whistle", "door"))
print(arb_longest_string())
