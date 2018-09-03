def print_spam(value):
    print(value)

def do_twice(value1, value2):
    print_spam(value1)
    print_spam(value2)

do_twice(print(print_spam),"kakak")
