def double_zero():
    import random
    array = [random.randint(0, 10) for i in range(int(input('Input list size:  ')))]
    print(array)
    for i in range(len(array)):
        if array[i] == 0:
            array.append(0)
            array.sort()
            print(array)

double_zero()