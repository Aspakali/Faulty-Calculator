n1=int(input("Enter your first number"))
n2=int(input("Enter your second number"))
opp=input("Choose operator (+ - * /)")
if opp=='+':
    if n1==56 and n2==9:
        print('77')
    else:
        print(n1+n2)
elif opp=='-':
    print(n1-n2)
elif opp=='*':
    if n1==45 and n2==3:
        print('555')
    else:
        print(n1*n2)
elif opp=='/':
    if n1==56 and n2==6:
        print('4')
    else:
        print(n1/n2)