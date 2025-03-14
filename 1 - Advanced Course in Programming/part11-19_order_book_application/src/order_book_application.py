# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id_value = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.finished = False
        self.workload = workload
        self.id = self.id_value
        Task.id_value += 1

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True
    
    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        programmers = []
        for order in self.orders:
            programmers.append(order.programmer)
        return list(set(programmers))

    def mark_finished(self, id: int):
        task = self.get_order_by_id(id)
        task.mark_finished()

    def get_order_by_id(self, id: int):
        for task in self.orders:
            if task.id == id:
                return task
        raise ValueError(f"Task with ID {id} not found.")

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished_count = 0
        unfinished_count = 0
        finished_hours = 0
        unfinished_hours = 0

        has_tasks = False

        for task in self.orders:
            if task.programmer == programmer:
                has_tasks = True
                if task.is_finished():
                    finished_count += 1
                    finished_hours += task.workload
                else:
                    unfinished_count += 1
                    unfinished_hours += task.workload

        if not has_tasks:
            raise ValueError(f"Programmer {programmer} has no tasks.")

        return (finished_count, unfinished_count, finished_hours, unfinished_hours)


class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split()
            workload = int(workload)
            self.order_book.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished_tasks(self):
        finished = self.order_book.finished_orders()
        if not finished:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def list_unfinished_tasks(self):
        unfinished = self.order_book.unfinished_orders()
        for task in unfinished:
            print(task)

    def mark_task_finished(self):
        try:
            task_id = int(input("id: "))
            self.order_book.mark_finished(task_id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def list_programmers(self):
        programmers = self.order_book.programmers()
        for programmer in programmers:
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            status = self.order_book.status_of_programmer(programmer)
            print(f"programmer: {programmer}")
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_task_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()


# Main entry point
application = OrderBookApplication()
application.execute()
