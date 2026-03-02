class PriorityQueue:
	def __init__(self, data):
		pass

	def get(self):
		pass

	def add(self, data):
		pass

	def peek(self):
		pass

#region Variation 1
"""
Variation 1: 
Binary Sort Queue Using the string value stored within a queued value
"""
class Queue:
    # Initialises self
    def __init__(self):
        self.queue = []

    # Adds value to the end of the queue
    def enqueue(self, data):
        self.queue.append(data)

    # Removes and returns the first (front) element from the queue
    def dequeue(self):
        if self.isEmpty:
            return "Queue is empty."
        else:
            return self.queue.pop(0)
    
    # Prints out the first (front) element in the stack
    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        else:
            return self.queue[0]

    # Bool check if the queue is empty or not    
    def isEmpty(self):
        return len(self.queue) == 0
    
    # returns the size of the queue
    def size(self):
        return len(self.queue)
queue_data = [
	("Robert", 1),
	("Jane", 4),
	("Alex", 2),
	("Robert", 1)
]
queue = Queue(queue_data)
sorted = []

for i in range(len(queue)):
	if i == 0:
		sorted.append(queue[0])
	else:
		for j in range(len(sorted)):
			if queue[i][1] < sorted[i][1]:
				sorted.insert(i+1, sorted[i])
			elif queue[i][1] > sorted[i][1]:
				sorted.insert(i-1, queue[i])

print(queue.get())
queue.add(("", 2))
print(queue.get())




#endregion

# queue_data = [
# 	("Robert", 1),
# 	("Jane", 4),
# 	("Alex", 2),
# 	("Robert", 1)
# ]
# queue = PriorityQueue(queue_data)

# print(queue.get())
# queue.add(("", 2))
# print(queue.get())