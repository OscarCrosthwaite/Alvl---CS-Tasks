class queue:
    def __init__(self):
        
        self.data = []
    #    self.fp = 0
    #    self.rp = -1

    #def __repr__(self) -> str:
    #    return_str = ""
    #    ptr = self.fp
    #    while ptr != (self.rp + 1) % self.max_size: 
    #        return_str += str(self.data[ptr]) + " "
    #        ptr = (ptr + 1) % self.max_size
    #    return return_str

    def isEmpty(self):
        return len(self.data) == 0


    def enqueue(self, item):
        self.data.append(item)
        

    def dequeue(self):
        if not self.isEmpty(self):
            return self.data.pop(0)
        else:
            print("Queue empty")

new_q1 = queue(5)
new_q2 = queue(7)


print(new_q1.data)
print(new_q2.data)


for num in range(11,15):
    new_q1.enqueue(num)
for num in range(101,106):
    new_q2.enqueue(num)


print(new_q1)
print(new_q1.data)
print(new_q2.data)


new_q1.enqueue(15)
new_q1.enqueue(16)
new_q2.enqueue(150)
new_q2.enqueue(160)


print(new_q1.data)
print(new_q2.data)

for _ in range(6):
    print(new_q1.dequeue)

for _ in range(8):
    print(new_q2.dequeue)

print(new_q1.data)
print(new_q2.data)


new_q1.enqueue(20)
new_q2.enqueue(200)


print(new_q1.data)
print(new_q2.data)

