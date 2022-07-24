def remove_duplicates():
    import random
    array = [random.randint(0, 10) for i in range(int(input('Input list size:  ')))]
    print(array)

    index = 1
    while index < len(array):
        if array[index] in array[ :index]:
            array.pop(index)
        else:
            index += 1
            print(array)

remove_duplicates()