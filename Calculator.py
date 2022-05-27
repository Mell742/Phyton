A = float(input("Enter the value of A: "))
op = input("enter the operator : ")
B = float(input("Enter the value of B: "))

if op == "+" :
    print("A + B =", A+B)
elif op == "-" :
    print("A - B =", A - B)
elif op == "/" :
    if B != 0 :
        print("A / B = ", A/B)
    else:
        print("You can't a number by 0")
elif op == "*" :
    print("A * B = ", A*B)

else:
    print("You've chosen the wrong operator")



