class Task:
    def __init__(self, description, term):
        self.description = description
        self.term = term
        self.status = False

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description} - {'Выполнено' if self.status else 'Не выполнено'} до {self.term}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, term):
        new_task = Task(description, term)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена.")

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description and not task.status:
                task.mark_as_done()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена или уже выполнена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")

task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание", "2024")  #
task_manager.add_task("Почистить ковер", "2024")
task_manager.show_current_tasks()
task_manager.mark_task_done("Сделать домашнее задание")
task_manager.show_current_tasks()