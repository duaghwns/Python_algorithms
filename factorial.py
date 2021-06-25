# 팩토리얼 구하기

# loop
import math


def factorial(n):
    a=1
    for i in range(n,0,-1):
        a *= i
    return a


# recursive call
a = 1
def fac(n):
    a = n * (n - 1)
    if(n==1):
        return a
    else:
        fac(n - 1)
        print(a)


print('반복문 : '+ str(factorial(5)))
print('재귀호출 : '+ str(fac(5)))
print('내장함수 : '+ str(math.factorial(5)))

