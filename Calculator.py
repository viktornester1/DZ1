a = float(input("Input first number"))
b = float(input("Input second number"))

print("""Select operation:
+
-
*
/
""")
c = str(input("You have chosen operation:"))

if (c == '+'):
    print(a + b)
elif (c == '-'):
    print(a - b)
elif (c == '*'):
    print(a * b)
elif (c == '/'):
    if(b == 0):
        print("cannot be divided by 0")
    else:
        print(a / b)











