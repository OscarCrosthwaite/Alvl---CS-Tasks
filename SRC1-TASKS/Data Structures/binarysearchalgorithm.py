def binarySearch(aList, itemSought):
		found = False
		index = -1
		first = 0
		last = len(aList)-1
		while first <= last and found == False:
			midpoint = (first + last) / 2
			if aList[midpoint] == itemSought:
				found = True
				index = midpoint
			else:	
				if aList[midpoint] < itemSought:
					first = midpoint + 1
				else:
					last = midpoint - 1
		return index
#