
def hello():
  print("Hello, you")

def pack(a, b, c):
  return [a, b, c]

def eat_lunch(list):
  if len(list) > 0:
    print(f"First I eat {list[0]}")
    print(f"Next I eat {list[1]}")
  else:
    print("My lunchbox is empty")

hello()
print(pack("socks", "barbed-wire", "7-up"))
eat_lunch(["tuna", "Apple Jacks"])
eat_lunch([])