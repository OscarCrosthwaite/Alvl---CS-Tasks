class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)

myList = [Node("",-1) for _ in range(5) ]
for index in range(4):
    myList[index].pointer = index + 1
myList[4].pointer = -1
start = 1
nextfree = -1
print(myList)


def addItem(newItem):
        myList[nextfree].name = newItem
        if start == -1:
            temp = myList[nextfree].pointer       
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:  
                myList[nextfree].pointer = start
                start = nextfree
            else:
                placeFound = False    
                while myList[p].pointer != -1 and placeFound == False:
                    if newItem >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placeFound = True
                temp = nextfree
                nextfree = Node[nextfree].pointer
                Node[temp].pointer = Node[p].pointer
                Node[p].pointer = temp


addItem("Colin")
addItem("Albert")
#addItem("Barry")
#addItem("Derek")
#addItem("Fred")
#addItem("Trevor",myList)

print(myList)