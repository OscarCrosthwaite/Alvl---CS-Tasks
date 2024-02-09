class TreeNode():
    def __init__(self, value, left = -1, right = -1) -> None:
        self.left = left
        self.right = right
        self.value = value
    #end constructor
#end record

treeList = []

def insertTreeNode(treeList, value):
    newNode = TreeNode(value)
    if len(treeList) == 0: #then root
        treeList[0] = newNode
    else:
        current = 0
        next = 0
        while next != -1:
            if value < treeList[current].value:
                next = treeList[current].left
                current =
            