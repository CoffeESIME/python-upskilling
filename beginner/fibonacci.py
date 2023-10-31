def fibo(n):
    
    #This is my first approach
    # """
    # Function that ask the user for a number of elements of the fibonacci sequence and generate them
    # """
    # elements = input("Please enter the number of elements that you want")
    # try:
    #     number = int(elements)
    #     if(number) < 0:
    #         print("you should ask for minumum one number of the sequence")
    #         exit()
    # except ValueError:
    #     print("the input is not a number")
    #     exit()
    # numbers = []
    # initializer = 0
    # latest=0
    # new_el =0
    # for element in range(1, number+1):
    #     if(element == 1):
    #         print(initializer)
    #     if(element==2):
    #         initializer = initializer +1
    #         latest=initializer
    #         print(initializer)
    #     elif(element>2):
    #         new_el = latest +initializer
    #         initializer= latest
    #         latest= new_el
    #         print(new_el)
#first approach
#fibo()

    """
    This a solutions with help
    Generate the first n elements of the Fibonacci sequence.
    
    Args:
    - n (int): Number of elements of the Fibonacci sequence to generate.
    
    Returns:
    - list: A list containing the first n elements of the Fibonacci sequence.
    """
    if n <= 0:
        print("You should ask for a minimum of one number of the sequence.")
        return
    
    if n == 1:
        return [0]
    
    # Initialize the first two Fibonacci numbers
    sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n
    for _ in range(2, n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
    
    return sequence


try:
    elements = int(input("Please enter the number of elements that you want: "))
    fibonacci_sequence = fibo(elements)
    if fibonacci_sequence:
        for num in fibonacci_sequence:
            print(num)
except ValueError:
    print("The input is not a valid number.")
