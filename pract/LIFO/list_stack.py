class Stack:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.insert(len(self.items), item)
    def remove(self):
        return self.items.pop(0)
    
    def __str__(self) -> str:
        return ", ".join(self.items)


q = Stack()
q.add("kot")
q.add("koshka")
q.add("sobak")
print(q)
q.remove()
print(q)
