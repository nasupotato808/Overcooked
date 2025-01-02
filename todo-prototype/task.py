from dataclasses import dataclass, field

@dataclass
class TodoItem:
    description: str
    complete: bool = False

    def __str__(self) -> str:
        c = "☑️" if self.complete else "⬜"
        return f"{c} {self.description}\n"

@dataclass
class TodoList():

    tasks: list[TodoItem] = field(default_factory=list)

    def is_empty(self):
        return len(self.tasks) == 0
    
    def __str__(self) -> str:
        tasks_str: list[str] = []
        for i in range(len(self.tasks)):
            t = self.tasks[i]
            indent = "  " if isinstance(t, Step) else ""
            tasks_str.append(f"{indent}{i+1}. {t}")
        return "".join(tasks_str)

    def add(self, task: TodoItem):
        self.tasks.append(task)

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
class Step(TodoItem):
    pass

@dataclass
class Task(TodoItem):
    steps: TodoList = field(default_factory=TodoList)
    
    def __str__(self):
        return f"{super().__str__()}{self.steps}\n"