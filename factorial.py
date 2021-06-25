
def factorial(n):
    a=1
    for i in range(n,0,-1):
        a *= i
    return a

print(factorial(5))