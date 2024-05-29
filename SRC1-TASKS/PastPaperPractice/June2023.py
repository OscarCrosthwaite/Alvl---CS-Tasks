class Treasure:
    def __init__(self, value:int, level:str) -> None:
        self.__value = value #private
        self.__level = level #private
    # end constructor

    def getValue(self) -> int:
        return self.__value
    # end function
    def getLevel(self) -> str:
        return self.__level
    # end function

    def setValue(self, value:int) -> None:
        self.__value = value
    # end procedure
    def setLevel(self, level:str) -> None:
        self.__level = level
    # end procedure

myTreasure = Treasure(500, "Gold")
print(myTreasure.getValue(), myTreasure.getLevel())        