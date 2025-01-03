from dataclasses import dataclass, field
from .strings import INDENT, NUMBERING, CHECKBOX

@dataclass
class Task:
    description: str
    complete: bool = False

    def __str__(self) -> str:
        return f"{CHECKBOX(self.complete)} {self.description}\n"
    
    def check(self) -> bool:
        self.complete = not self.complete
        return self.complete
    
    def edit(self, new_desc) -> str:
        old_desc = self.description
        self.description = new_desc
        return old_desc

@dataclass
class TaskList():

    tasks: list[Task] = field(default_factory=list)

    def is_empty(self) -> bool:
        return len(self.tasks) == 0
    
    def __len__(self) -> int:
        return len(self.tasks)

    def __str__(self) -> str:
        tasks_str: list[str] = []
        for i in range(len(self.tasks)):
            t = self.tasks[i]
            indent = INDENT if isinstance(t, Step) else ""
            tasks_str.append(f"{indent}{NUMBERING(i+1)} {t}")
        return "".join(tasks_str)
    
    def get_task(self, idx: int) -> Task:
        return self.tasks[idx]

    def add(self, task: Task) -> None:
        self.tasks.append(task)
    
    def delete(self, idx) -> Task:
        return self.tasks.pop(idx)

@dataclass
class Step(Task):
    pass

@dataclass
class Todo(Task):
    steps: TaskList = field(default_factory=TaskList)
    
    def __str__(self) -> str:
        return f"{super().__str__()}{self.steps}"