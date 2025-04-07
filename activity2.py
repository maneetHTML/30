class employee : #parent
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun (self):
        print("Hello",self.name)
class test (employee): # child
    def __init__(self,name,age,sal):
        super().__init__(name,age)
        self.sal=sal
obj=test("maneet","12",'750')
print(obj.name)
print(obj.age)
print(obj.sal)
obj.fun()