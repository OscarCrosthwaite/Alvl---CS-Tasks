class Animal:
    #private age
    #private vertebrae

    #public procedure sound
    
    def __init__(self, vertebrae) -> None:
        self.age = 0                #private
        self.vertebrae = vertebrae  #private
    #end public constructor

    def sound(self):
        pass
    #end public procedure
#end class

class Mammal(Animal):
    def __init__(self, legs, ) -> None:
        self.legs = legs
        super().__init__(True)
    #end constructor
#end class

class Cat(Mammal):
    def sound(self):
        print("Meow")
    #end public procedure
#end clas

class Dog(Mammal):
    def sound(self):
        print("Woof")
    #end public procedure
#end class


seed_list = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
obj_list = []
for seed in seed_list:
    if seed == 1:
        obj_list.append(Cat(4))
    else:
        obj_list.append(Dog(4))
    #endif
#next seed

for animal in obj_list:
    animal.sound()
#next animal
