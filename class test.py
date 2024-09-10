

class human():
    def __init__(self,height,age):
        self.height = height
        self.age = age

    def growth(self):
        print(int(self.height)/int(self.age))
    

bob = human("165", "50")
sam = human("140","16")
print(bob.age)
print(sam.age)
print(sam.growth())
