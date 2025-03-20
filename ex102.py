# Python Exercise #102 - Function for Factorial

def factorial(num, show = True):
    """
       Calculate the factorial of a number with an option to show the calculation process.

       Parameters:
       num (int): The number to calculate the factorial.
       show (bool): If True, shows the calculation steps. Default is True.

       Returns:
       int: The factorial result.
       """
    total = 1
    for i in range(num, 0, -1):
        total *= i
        if show:
            print(f'{i} x ' if i > 1 else f'{i} = ', end='')
    return total

print(factorial(5))