# 함수 장식자(function decorator) : meta 기능이 있음
# 장식자는 또 다른 함수를 감싼 함수다.

def make2(fn):
    return lambda:'안녕 ' + fn()

def make1(fn):
    return lambda:'반가워 ' + fn()

def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi())

print()
@make2
@make1
def hello2():
    return '고길동'

print(hello2())

print()
hi2 = hello2()
print(hi2)

print()
hi3 = hello2()
print(hi3)

# 문제) 근속년수에 따른 급여수령액 계산하기
import time
def inputfunc():
    datas=[]
    now=time.localtime()
    now_y=now.tm_year
    while True:
        con=input("계속하시겠습니까?(y/n)")
        if con=='n': return datas
        empno,name,baseSal,hireDate=input().split(",")
        data={}
        empno,baseSal,hireDate=map(int,[empno,baseSal,hireDate])
        data['사번']=empno
        data['기본급']=baseSal
        data['이름']=name
        #LOS Length of service 근속년수
        LOS=now_y-hireDate
        data['근무년수']=LOS
        #LSA long-service allowance 근속수당
        if 0<=LOS<4: LSA=150000
        elif 4<=LOS<9: LSA=450000
        else: LSA=1000000
        data['근속수당']=LSA
        TotalSal=LSA+baseSal
        #AD amount deducted 공제액
        if TotalSal<2000000: AD=TotalSal*0.0015
        elif TotalSal<3000000: AD=TotalSal*0.003
        else: AD=TotalSal*0.005
        data['공제액']=AD
        data['수령액']=TotalSal-AD
        datas.append(data)
datas=inputfunc()
def processfunc(datas):
    datas.sort(key=lambda x:x['사번'])
    for data in datas:
        print(data)
    print('처리건수 : ',len(datas),"건")

processfunc(datas)