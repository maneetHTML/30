class employee : #parent
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun (self):
        print("Hello",self.name)
class test (employee): # child
    pass
class car (employee): # child
    pass
obj=car("maneet","12")
print(obj.name)
print(obj.age)
obj.fun()