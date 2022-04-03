# 반복문 for와 range()
# range(초기치, 목적치, 증가치) : 수열 생성 함수
print(list(range(1, 6, 1)))
print(list(range(1, 6)))
print(set(range(1, 6)))
print(tuple(range(1, 6)))
print(list(range(6)))
print(list(range(0, 6)))
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))

print()
for i in range(6):
    print(i, end = ' ')
    
print()
for i in range(1, 10):   # java : for(int i=1; i <=10; i++){ }
    print('{0}*{1}={2}'.format(2, i, i * 2), end = ' ')
    
print()
tot = 0
for i in range(1, 11):
    tot += i

print('합은 ' + str(tot))

print('합은 ' + str(sum(range(1, 11))))

# 참고 : n-gram : 문자열에서 n개의 연속된 요소를 추출하기
# 문자 단위 2 - gram
text = 'hello'

for i in range(len(text)):
    print(text[i:i+2])
    
print()
# 단어 단위
text = 'this is python program'
words = text.split()
print(words)

for i in range(len(words) - 1):
    print(words[i], words[i + 1])
    
# 문1) 2 ~ 9 단 모두 출력
for n in range(2, 10):
    print('--{}단--'.format(n))
    for i in range(1, 10):
        print('{0}*{1}={2}'.format(n, i, i * n))
# 문2) 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
hap = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        # print(i)
        hap += i
print(hap)
# 문3) 주사위를 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 예) (1, 3), (2, 2)
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) % 4 == 0:
            print('({0}, {1})'.format(i, j))
