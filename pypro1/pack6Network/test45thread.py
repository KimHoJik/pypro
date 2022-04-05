# Thread
# process는 실행가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하면서 task라고 부른다.
# process의 작은 실행단위를 thread라고 한다. thread 기법을 이용하면 여러 개의 thread를 통해 여러 개의 작업을 할 수 있다.
# multi thread에 의한 multi tasking이 가능함

import threading, time

def run(id):
    for i in range(1, 11):
        print('id = {}-->{}'.format(id, i))
        time.sleep(0.5)
        
# 1) thread X
# run('일')    # 순차적
# run('이')

# 2) thread O
th1 = threading.Thread(target = run, args = ('일',)) 
th2 = threading.Thread(target = run, args = ('이',))
th1.start()
th2.start() 

# 메인 thread가 맨 나중에 수행하도록 만드는 thread의 join 함수
th1.join()
th2.join()

print('프로그램 종료')