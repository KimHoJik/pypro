# class

kor = 100

def abc():
    print('함수라고 해')
    
class MyClass:
    kor = 90
    
    def abc(self):
        print('난 메소드야~')
        
    def show(self):
        # kor = 88
        print(self.kor)
        print(kor)
        self.abc()
        
my = MyClass()
my.show()

print('------------')