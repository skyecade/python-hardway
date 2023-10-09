def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("arg1: " + arg1 + ", arg2: " + arg2 + " <--- alternative")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")


print_two("Bob", "Meg")
print_two_again("Cam", "Zack")
print_one("Bill")
print_none()