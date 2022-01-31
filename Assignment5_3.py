class Arithmatic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=float(input("Enter first number: "))
        self.Value2=float(input("Enter second number: "))

    def Addition(self):
        ans=self.Value1+self.Value2
        return ans

    def Subtraction(self):
        sub=self.Value1-self.Value2
        return sub

    def Multiplication(self):
        mult=self.Value1*self.Value2
        return mult

    def Division(self):
        div=(self.Value1)/(self.Value2)
        return div

def main():
    obj=Arithmatic()
    obj.Accept()
    add=obj.Addition()
    sub=obj.Subtraction()
    mult=obj.Multiplication()
    div=obj.Division()

    print(add,sub,mult,div)

    obj2=Arithmatic()
    obj2.Accept()
    add=obj2.Addition()
    sub=obj2.Subtraction()
    mult=obj2.Multiplication()
    div=obj2.Division()

    print(add,sub,mult,div)

if __name__=="__main__":
    main()
