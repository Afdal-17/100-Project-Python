op = input("Masukan operasi bilangan: ")
op1 = int(input("Masukan angka 1: "))
op2 = int(input("Masukan angka 2: "))

if op == "+":
    print(op1 + op2)
elif op == "-":
    print(op1 - op2)
elif op == "*":
    print(op1 * op2)
elif op == "/":
    print(op1 / op2)
elif "/"== op2 != 0:
    print(op1/op2)
else:
    print("Error!")