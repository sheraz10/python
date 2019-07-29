class Charactercount:
    var=""

    def func1(self,s):
        if isinstance(s,int):
            print(" Invalid Input")
            exit()
        else:
            self.var=s

    def func2(self):
        count =len(self.var)
        return count



s=12
obj=Charactercount()

obj.func1(s)
res=obj.func2()


print("Number of characters: " + str(res))
