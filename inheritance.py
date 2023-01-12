'''
##########################################################
#                   SINGLE INHERITANCE
##########################################################
print("Single Inheritance : ")
print()
class ParentClass:
    def parent(self):
        self._b = 200
        print("This is parent class")

    def mother(self):
        self._a = 100
        print(self._a)
        print(self._b)

class ChildClass(ParentClass):
    
    def child(self):
        print("This is child class")

child_obj = ChildClass()

child_obj.child()
child_obj.parent()
child_obj.mother()
print("_"*25)
##########################################################
#                   MULTI LEVEL INHERITANCE
##########################################################
print("Multi Level Inheritance : ")
print()
class GrandpaClass:
    def grandpa1(self):
        print("This is grandpa class")

class ParentClass1(GrandpaClass):
    
    def parent1(self):
        print("This is parent class")

class ChildClass1(ParentClass1):
    def child1(self):
        print("This is child class")

child_obj1 = ChildClass1()
child_obj1.child1()
child_obj1.parent1()
child_obj1.grandpa1()
'''
##########################################################
#                   MULTIPLE INHERITANCE
##########################################################
print("Multiple Inheritance : ")
print()
class FatherClass:
    def father1(self):
        print("This is father class")

class MotherClass:
    
    def mother1(self):
        print("This is moher class")

class ChildClass2(FatherClass,MotherClass):
    def child1(self):
        print("This is child class")

child_obj1 = ChildClass2()
child_obj1.child1()
child_obj1.father1()
child_obj1.mother1()
print("_"*25)
##########################################################
#                   HIERARCHICAL INHERITANCE
##########################################################
print("Hierarchical Inheritance : ")
print()
class ParentClass2:
    def parent2(self):
        print("This is parent class")

class SonClass1(ParentClass2):
    def son1(self):
        print("This is first son class")
class SonClass2(ParentClass2):
    def son2(self):
        print("This is second son class")

son1_obj = SonClass1()
son1_obj.son1()
son1_obj.parent2()

son2_obj = SonClass2()
son2_obj.son2()
son2_obj.parent2()