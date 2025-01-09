from time import sleep 
from colorama import Fore, Style, init
from alive_progress import alive_bar

init(autoreset=True)

while True:


    class User:
        def __init__(self, username, password):
            self.username = username
            self.password = password

    class Task:
        def __init__(self, title, description, priority):
            self.title = title
            self.description = description
            self.priority = priority

        def display_task(self):
            color = Fore.RED if self.priority == "High" else Fore.YELLOW if self.priority == "Medium" else Fore.GREEN
            return f"{color}Title: {self.title}, Priority: {self.priority}\nDescription: {self.description}"

    class HomeTask(Task):
        def __init__(self, title, description, priority, room):
            super().__init__(title, description, priority)
            self.room = room

        def display_task(self):
            return super().display_task() + f"\nRoom: {self.room}"

    class WorkTask(Task):
        def __init__(self, title, description, priority, deadline):
            super().__init__(title, description, priority)
            self.deadline = deadline

        def display_task(self):
            return super().display_task() + f"\nDeadline: {self.deadline}"

    tasks = []

    def login():
        print(Fore.CYAN + "=== Login ===")
        retry = True
        while retry:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username and password:
                retry = False
            else:
                print(Fore.RED + "Invalid login details. Please try again.")
        print(Fore.YELLOW + "Logging in...")
        sleep(2)
        with alive_bar(100) as bar:
            for i in range(100):
                sleep(0.025)
                bar()
        print(Fore.GREEN + "Successfully logged in!\n")
        return User(username, password)

    def process(description, total_steps=10):
        print(Fore.YELLOW + description)
        with alive_bar(total_steps) as bar:
            for _ in range(total_steps):
                sleep(0.25)
                bar()

    def add_task():
        print(Fore.CYAN + "=== Add Task ===")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = input("Enter priority (Low/Medium/High): ")
        category = input("Choose category (Home/Work): ")

        if category.lower() == "home":
            room = input("Enter room: ")
            task = HomeTask(title, description, priority, room)
        elif category.lower() == "work":
            deadline = input("Enter deadline (dd-mm-yyyy): ")
            task = WorkTask(title, description, priority, deadline)
        else:
            print(Fore.RED + "Unknown category!")
            return

        tasks.append(task)
        process("Adding task...")
        print(Fore.GREEN + "Task added!\n")

    def display_tasks():
        print(Fore.CYAN + "=== Task List ===")
        process("Processing task list...")
        if not tasks:
            print(Fore.RED + "No tasks found!")
        else:
            for idx, task in enumerate(tasks, 1):
                print(Fore.YELLOW + f"\nTask {idx}:")
                print(task.display_task())

    def delete_task():
        print(Fore.CYAN + "=== Delete Task ===")
        display_tasks()
        retry = True
        while retry:
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    process("Deleting task...")
                    deleted_task = tasks.pop(task_number - 1)
                    print(Fore.GREEN + f"Task deleted: {deleted_task.title}")
                    retry = False
                else:
                    print(Fore.RED + "Invalid task number!")
            except ValueError:
                print(Fore.RED + "Invalid input!")

    def main():
        user = login()
        while True:
            print(Fore.CYAN + "\n=== Task Manager ===")
            print("1. Add Task")
            print("2. Display Tasks")
            print("3. Delete Task")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                add_task()
            elif choice == "2":
                display_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print(Fore.GREEN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice!")

    if __name__ == "__main__":
        main()