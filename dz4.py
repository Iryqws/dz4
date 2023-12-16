class Parents1:
    def weight(self):
     print(66)
class Parents2:
    def height(self):
     print(180)

class Mom(Parents1):
    def weight(self):
     print(49)

class Dad(Parents2):
    def height(self):
     print(180)

class Child(Mom, Dad):
    weight = 35
    age = 8
