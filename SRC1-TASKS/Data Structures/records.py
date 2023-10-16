student1t = ("Dave", "Bloggs", 18, True)
student2t = ("Fred", "Smith", 16, False)


class Student_record:
    def __init__(self):
        self.firstname = ""
        self.lastname= ""
        self.age = 0
        self.registered = False
    #end constructor
#end class

student1 = Student_record()
student1.firstname = "Dave"
student1.lastname = "Bloggs"
student1.age = 18
student1.registered = True


student2 = Student_record()
student2.firstname = "Fred"
student2.lastname = "Smith"
student2.age = 16
student2.registered = False

print(student1t[2])

def addone(x):
    x = x + 1
    return x
#endfunction

newage = addone(student2.age)
print(newage)
