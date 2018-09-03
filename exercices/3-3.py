def do_four():
    for x in range(0, 4):
        print('|',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', '|')

def do_one():
    print('+','-', '-', '-', '-', '+','-', '-', '-', '-', '+')

def print_grade():
    do_one()
    do_four()
    do_one()
    do_four()
    do_one()


print_grade()
