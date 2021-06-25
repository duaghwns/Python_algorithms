# 팩토리얼 구하기
import math

# loop
def factorial(n):
    a=1
    for i in range(n,0,-1):
        a *= i
    return a


# recursive call
def fac(n):
    if(n==1):
        return n
    else:
        a = n * fac(n-1)
        return a


print('반복문 : '+ str(factorial(5)))
print('재귀호출 : '+ str(fac(5)))
print('내장함수 : '+ str(math.factorial(5)))