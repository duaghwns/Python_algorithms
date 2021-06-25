
# 반복문
def loop(n):
    a = 0
    for i in range(n+1):
        a += i
    return a

print(loop(100))

# 가우스 공식
def gauss(n):
    return (1+n)*(n/2)

print(gauss(100))