from dataclasses import dataclass

class TaskList:
    def __init__(self):
        self.tasks = []

@dataclass
class Task:
    description: str
    complete: bool = False
