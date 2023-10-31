def fibo():
    """
    Function that ask the user for a number of elements of the fibonacci sequence and generate them
    """
    elements = input("Please enter the number of elements that you want")
    try:
        number = int(elements)
        if(number) < 0:
            print("you should ask for minumum one number of the sequence")
            exit()
    except ValueError:
        print("the input is not a number")
        exit()
        # print(number)
    numbers = []
    initializer = 0
    latest=0
    new_el =0
    for element in range(1, number+1):
        if(element == 1):
            print(initializer)
        if(element==2):
            initializer = initializer +1
            latest=initializer
            print(initializer)
        elif(element>2):
            new_el = latest +initializer
            initializer= latest
            latest= new_el
            print(new_el)
        


fibo()
