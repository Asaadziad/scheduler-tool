from datetime import date

class task:
    def __init__(self,name : str ,isFinished : bool) -> None:
        self.name = name
        self.isFinished = isFinished
        self.date = date.today()
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Date: {self.date}, Done: [ {self.isFinished} ]"
    
    def setName(self,new_name: str) -> None:
        self.name = new_name
    def setIsFinished(self, isFinished : bool) -> None:
        self.isFinished = isFinished

def editTask(old_task: task, new_name: str, task_finished: bool) -> None:
    old_task.setName(new_name)
    old_task.setIsFinished(task_finished)

def addNewTask(tasks: list, new_task : task) -> None:
    tasks.append(new_task)

def displayTasks(tasks: list) -> None:
    x = 0
    while(x < len(tasks)):
        print(tasks[x])
        x = x+1

# tasks is a list of lists (2D matrix) where each list represent a row in the grid
# and each i in tasks[j]: list, is a column in the grid
tasks = []

t = task("fix this shit", False)

addNewTask(tasks, t)
editTask(t, "help me", False)
displayTasks(tasks)