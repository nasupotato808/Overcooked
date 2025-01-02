from dataclasses import dataclass

class ToDoList:

    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return len(self.tasks) == 0
    
    def add(self, task):
        self.tasks.append()

    def check(self, idx: int):
        self.tasks[idx].complete = not self.tasks[idx].complete
        return self.tasks[idx].complete
    
    def edit(self, idx: int, new_desc: str):
        old_desc = self.tasks[idx].description
        self.tasks[idx].description = new_desc
        return old_desc
    
    def get_description(self, idx):
        return self.tasks[idx].description
    
    def swap(self, idxA, idxB):
        self.tasks[idxA], self.tasks[idxB] = self.tasks[idxB], self.tasks[idxA]
    
    def delete(self, idx):
        return self.tasks.pop(idx)

@dataclass
class ToDoItem:
    description: str
    complete: bool = False

@dataclass
class Task(ToDoItem):
    steps: ToDoList = ToDoList()
