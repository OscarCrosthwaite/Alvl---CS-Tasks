# creates queue with MAX_SIZE (five) number of elements
MAX_SIZE = 5
q1 = [0 for _ in range(MAX_SIZE)]
# creates variables that determine positions of elements in queue
q1_size = 0
q1_fp = 0
q1_rp = -1

def isEmpty():
    # q1_size is using the global variable, rather than creating a local variable
    global q1_size
    # returns true if queue-1 is empty
    return q1_size == 0

def isFull():
    global MAX_SIZE
    global q1_size
    #returns true if queue-1 is full
    return MAX_SIZE == q1_size

def enqueue(item):
    # checks if queue is full
    if not isFull():
        # increases size and rearpoint value
        q1_rp = (q1_rp + 1) % MAX_SIZE
        q1_size += 1
        # adds item to the list
        q1[q1_rp] = item

def dequeue():
    if not isEmpty():
        item_p = q1_fp
        q1_fp = (q1_fp + 1) % MAX_SIZE
        q1_size = q1_size - 1
        return q1[item_p]    

for num in range(11, 16):
