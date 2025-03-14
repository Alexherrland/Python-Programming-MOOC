# Write your solution here:
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
