class Queue:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.insert(0, item)
    def remove(self):
        return self.items.pop()
    
    def __str__(self) -> str:
        return ", ".join(self.items)

q = Queue()
q.add("kot")
q.add("koshka")
q.add("sobak")
print(q)
q.remove()
print(q)