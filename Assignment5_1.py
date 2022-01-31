class Demo:

    Value=10

    def __init__(self,value1,value2):
        self.no1=value1
        self.no2=value2

    def Fun(self):
        print(self.no1)

    def Gun(self):
        print(self.no2)

def main():
    Obj1=Demo(11,21)
    Obj1.Fun()
    Obj1.Gun()

    Obj2=Demo(51,101)
    Obj2.Fun()
    Obj2.Gun()

if __name__=="__main__":
    main()
