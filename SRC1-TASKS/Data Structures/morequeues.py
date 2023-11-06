class Queue_data:
    def __init__(self,max_size):
        self.max_size = max_size
        self.data = [0 for _ in range(self.max_size)]
        self.size = 0
        self.fp = 0
        self.rp = -1
    #end constructor
    def __repr__(self) -> str:
        return_str = ""
        ptr = self.fp
        while ptr != (self.rp + 1) % self.max_size: 
            return_str += str(self.data[ptr]) + " "
            ptr = (ptr + 1) % self.max_size
        #end while
        return return_str
    #end function
            
#end record
def isEmpty(q):
    return q.size == 0
#end function
def isFull(q):
    return q.max_size == q.size
#end function
def enqueue(item,q):
    if not isFull(q):
        q.rp = (q.rp + 1) % q.max_size
        q.size += 1
        q.data[q.rp] = item
    else:
        print("queue full")
    #end if
#end procedure
def dequeue(q):
    if not isEmpty(q):
        item_p = q.fp
        q.fp = (q.fp + 1) % q.max_size
        q.size -= 1
        return q.data[item_p]
    else:
        print("Queue empty")
    #end if
#end function
new_q1 = Queue_data(5)
new_q2 = Queue_data(7)
print(new_q1.data)
print(new_q2.data)
for num in range(11,15):
    enqueue(num,new_q1)
#next num
for num in range(101,106):
    enqueue(num,new_q2)
#next num
print(new_q1)
print(new_q1.data)
print(new_q2.data)
enqueue(15,new_q1)
enqueue(16,new_q1)
enqueue(150,new_q1)
enqueue(160,new_q2)
print(new_q1.data)
print(new_q2.data)
for _ in range(6):
    print(dequeue(new_q1))
#next _
for _ in range(8):
    print(dequeue(new_q2))
#next _
print(new_q1.data)
print(new_q2.data)
enqueue(20,new_q1)
enqueue(200,new_q2)
print(new_q1.data)
print(new_q2.data)
print(new_q1)
