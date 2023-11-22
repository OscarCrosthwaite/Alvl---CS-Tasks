class Node:
    def __init__(self, name, pointer) -> None:
        self.name = name
        self.pointer = pointer
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
    def getName(self):
        return self.name
    def getPointer(self):
        return self.pointer

myList = [Node("",-1) for _ in range(5) ]
for index in range(4):
    myList[index].pointer = index + 1
myList[4].pointer = -1



nextfree = 1
start = 0

def addItem(s_newItem, s_nextfree, s_start):
    myList[s_start].name = s_newItem
    if s_nextfree == -1:
        temp = myList[s_nextfree].pointer
        myList[s_nextfree].pointer = 
        s_start = s_nextfree
        s_nextfree = temp
        return s_start and s_nextfree
    else:
        p = s_start
        if newItem < myList[p].name:
            myList[s_nextfree].pointer = s_start
            s_start = s_nextfree
        else:
            placeFound = False
            while myList[p].pointer != -1 and placeFound == False:
                if newItem >= myList[myList[p].pointer].name:
                    p = myList[p].pointer
                else:
                    placeFound = True
            temp = s_nextfree
            s_nextfree = myList[temp].pointer
            myList[temp].pointer = myList[p].pointer
            myList[p].pointer = temp

addItem("Colin", nextfree, start)
addItem("Albert", nextfree, start)
print(myList)