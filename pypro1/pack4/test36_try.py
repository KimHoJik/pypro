# 에러 발생에 따른 예외 처리
# logic error, exception error : 파일, 네트워크, db, 키보드 ...

def divide(a, b):
    return a / b

print('뭔가를 하다가 ...')
# c = divide(5, 2)
# c = divide(5, 0)
# print(c)

try:
    c = divide(5, 2)
    # c = divide(5, 0)
    print(c)
    
    aa = [1, 2]
    # print(aa[2])

    open('c:/abc.txt')
    
except ZeroDivisionError:
    print('두번째 숫자는 0 안돼~')
except IndexError as er:
    print('참조 범위 오류 : ', er)
except Exception as e:  # 여기로 에러를 처리할 예정
    print('에러 처리 : ', e)
finally:
    print('에러와 상관없이 반드시 수행')
    
print('종료')