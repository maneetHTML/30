class employee : #parent
    def __init__(self,car,mod):
        self.car=car
        self.mod=mod
    def fun (self):
        print("bye sir")
class test (employee): # child
    def __init__(self,name,age,price):
        super().__init__(name,age)
        self.price=price
obj=test("2025","bmw",'2,000,000')
print(obj.car)
print(obj.mod)
print(obj.price)
obj.fun()