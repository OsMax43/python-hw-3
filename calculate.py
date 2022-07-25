print("Для завершение программы введи ноль в поле 'знак'")

while True:
    c = input("Введи знак (+, -, *, /):  ")
    if c == "0":
        break
    if c not in ('+','-', '*', '/'):
        continue
    a = float(input("a =  "))
    b = float(input("a =  "))

    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)

    elif c == "/":
        if b != 0:
         print(a / b)
        else:
            print("Деление на 0 !")
