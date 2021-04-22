class Math:
    var1=0
    var2=0
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2        
    def mul(self):
        print(self.var1*self.var2)
obj1=Math(12,24)
obj2=Math(12,4)
obj2.mul()