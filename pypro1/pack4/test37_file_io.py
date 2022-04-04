# 파일 단위로 읽고 저장
import os 

print(os.getcwd())  # 프로젝트에 대한 경로

try:
    print('파일 읽기')
    f1 = open(r'C:\pwork\psou\pypro\pypro1\pack4\abc.txt', mode='r', encoding='utf-8')
    print(f1)
    print(f1.read())
    f1.close()
except Exception as e:
    print('에러 : ', e)