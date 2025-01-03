def print_calc():
    logo = """
        _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .---------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      ___      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /   \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / / \ \    | || |    | |       | || |  / .'   \ |  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____\ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /     \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|   |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |               | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '-------------- ' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    `
    """
    print(logo)
print_calc()


def calc(first, second, operation):
    if operation == '+':
        return first+second
    elif operation == '-':
        return first-second
    elif operation == '*':
        return first*second
    elif operation == '/':
        if second != 0:
            return first/second
        else:
            return "invalid"
    else:
        return "cannot calculate"
def calculator1():
    print("What's the first number?:")
    n1= float(input())
    return n1
def calculator2():
    print("Pick an operation:")
    operation= input()
    print("What's the next number?:")
    n2= float(input())
    return operation,n2


x=calculator1()
o,y=calculator2()
ans = calc(x,y,o)
print(x,o,y,'=',ans)


while(True):
    print("Type 'y' to continue calculating with ans, or type 'n' to start a new calculation:")
    z=input()
    if z=='n':
        x=calculator1()
        o,y=calculator2()
        ans = calc(x,y,o)
        print(x,o,y,'=',ans)
        
    if z=='y':
        x=ans
        o,y=calculator2()
        ans= calc(x,y,o)
        print(x,o,y,'=',ans)
        
