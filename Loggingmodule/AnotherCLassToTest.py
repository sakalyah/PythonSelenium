

class AnotherClass():

    def __init__(self,Harish):
        self.name = Harish

    def test(self,a):

        if a == self.name :
            print(self.name+" is present")
            return self.name
        else :
            print(self.name+ " is not present")
            return None
