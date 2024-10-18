from datetime import datetime


class Todo:
    def __init__(self, task, category, date_added=None, date_comleted=None, status=None, position=None):
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.now().isoformat()
        self.date_completed = date_comleted
        self.status = status if status is not None else 1  # 1 for pending, 2 for completed
        self.position = position

    def __repr__(self) -> str:
        return f"({self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status},{self.position})"
