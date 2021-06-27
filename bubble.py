list = [7,5,8,3,1,9,2,6,4]

# 버블정렬
def bubble(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i]<=li[j]:
                tmp =  li[j]
                li[j] = li[i]
                li[i] = tmp
    return li

print(bubble(list))