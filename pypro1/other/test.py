for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')

print()
print(5 / 3)
print(5 // 3)
print(5 % 3)

print()
v1, *v2, v3 = [1, 2, 3, 4, 5]
print(v1)
print(v2)
print(v3)

print(list(range(1, 6, 2)))

dan = 3
while dan < 10:
    a=1
    if dan % 2 == 1: 
        while a < 10:
            print(dan,'*',a,'=',dan * a)
            a += 1
    print()
    dan += 1
    
print()
def func():
    a = 0
    for i in range(1, 101):
        if i % 5 == 0:
            a += i
        
    return a    
print(func())

a = 0   # 홀수의 합
b = 0   # 홀수의 갯수
for i in range(1, 101):
    if i % 2 == 1:
        a += i
        b += 1
    
print('홀수의 합 : ',a)
print('홀수의 갯수 : ',b)

def func1():
    a = 1
    total = 0
    count = 0
    while a < 101:
        if a % 2 == 0:
            total += a
            count += 1
        a += 1
    
    return total, count

print(func1())

for i in [1, 2]:
    for j in [1, 2]:
        if (i + j) % 2 == 0:
            print('{0} {1}'.format(i, j))
