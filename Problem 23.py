n = int(input("To how many places would you like to print the fibonacci sequence? "))

def Fibonacci(n):
    lst = [0]
    if n == 1:
        return lst
    else:
        lst.append(1)
        for _ in range(n-2):
            lst.append(lst[-2] + lst[-1])
    print(f"Fibonacci in reverse order: {str(lst[::-1]).strip('[]')}")
    print(f"Length of fibonacci sequence: {len(lst)}")
    print(f"Original fibonnaci sequence:  {str(lst).strip('[]')}")
    
Fibonacci(n)