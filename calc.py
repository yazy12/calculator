def add(x, y):
    print(x+y)
def sub(x, y):
    print(x-y)
def div(x,y):
    print(x/y)
def mul(x, y):
    print(x*y)
operator = input("+/1, -/2, ÷/3, x/4: ")
first_num = int(input("enter first number: "))
sec_num = int(input(" enter second number: "))

if operator == '1':
    add(first_num, sec_num)
if operator == '2':
    sub(first_num, sec_num)
if operator == '3':
    div(first_num, sec_num)
if operator == '4':
    mul(first_num, sec_num)
