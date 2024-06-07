class Person:
    def __init__(self, age, skill):
        self.age = age
        self.skill = skill

    def __lt__(self, other):
        if self.skill == other.skill:
            return self.age > other.age  
        return self.skill > other.skill  

    def __str__(self):
        return f"Person(Age={self.age}, Skill={self.skill})"

class PriorityQueue:
    def __init__(self):
        self.heap = []
    Largest = 0

    def max_heapify(self, i):
        left = (2 * (i)) + 1
        right = (2 * (i)) + 2
        # i = i - 1
        # largest = 0
        global Largest
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            largest = left
        else:
            Largest = i
        if right < len(self.heap) and self.heap[right] > self.heap[Largest]:
            Largest = right
        if Largest != i:
            k = self.heap[i]
            self.heap[i] = self.heap[Largest]
            self.heap[Largest] = k
            self.max_heapify(Largest + 1)



        # if largest != i:
        #     node.heap[i], node.heap[largest] = node.heap[largest], node.heap[i]
        #     node.max_heapify(largest)

    def build_max_heap(self):
        n = len(self.heap)
        for i in range((n // 2) , 0, -1):
            self.max_heapify(i)


    def add_Person(self, Person):
        self.heap.append(Person)
        self.build_max_heap()

    def pop_Person(self):
        if len(self.heap) == 0:
            print("empty")
        self.build_max_heap()
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        
        return max

    def increase_skill(self, Person):
        index = self.heap.index(Person)
        if index != -1:
            self.heap[index].skill = chr(ord(self.heap[index].skill) + 1)
            self.build_max_heap()

    def print_Person(self):
        for Person in self.heap:
            print(Person)

if __name__ == "__main__":
    pq = PriorityQueue()
    p1 = Person(25, 'f')
    p2 = Person(25, 'A')
    p3 = Person(22, 'H')
    p4 = Person(25, 'W')

    pq.add_Person(p1)
    pq.add_Person(p2)
    pq.add_Person(p3)
    pq.add_Person(p4)

    print(pq.pop_Person())  # Candidate(Age=22, Skill=C)
    pq.increase_skill(p2)
    print(pq.pop_Person())  # Candidate(Age=25, Skill=B)
    print(pq.pop_Person())  # Candidate(Age=30, Skill=B)
    print(pq.pop_Person())  # Candidate(Age=30, Skill=B)
        
    
