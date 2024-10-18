import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()


def create_table():
    c.execute("""
              CREATE TABLE IF NOT EXISTS todos (
                  task text,
                  category text,
                  date_added text,
                  date_completed text,
                  status integer,
                  position integer
                  )
              """)


create_table()


def insert_todo(todo: Todo):
    # get position of a todo
    c.execute('select count(*) from todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        # todo_value = (todo.task, todo.category, todo.date_added, todo.date_completed, todo.status, todo.position)
        c.execute("""
                  INSERT INTO todos VALUES (?,?,?,?,?,?)
                  """, (todo.task, todo.category, todo.date_added, todo.date_completed, todo.status, todo.position))


def get_a_todo(position: int):
    c.execute('SELECT * FROM todos WHERE position=?', (position,))
    row = c.fetchone()
    return Todo(*row) if row else None


def getall_todos() -> List[Todo]:
    c.execute('SELECT * FROM todos')
    rows = c.fetchall()
    todos = []

    for r in rows:  # r is a tuple
        todos.append(Todo(*r))

    return todos


def delete_todo(position: int):
    c.execute('select count(1) from todos')
    count = c.fetchone()[0]

    with conn:
        c.execute('DELETE FROM todos WHERE position=?', (position,))
        # changing order of the list
        for pos in range(position + 1, count):
            change_position(pos, pos-1, False)


def change_position(old_pos, new_pos, commit=True):
    c.execute('update todos set position=? where position=?', (new_pos, old_pos))

    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task = :task, category = :category WHERE position = :position',
                      {'position': position, 'task': task, 'category': category})
        elif task is not None:
            c.execute('UPDATE todos SET task = :task WHERE position = :position',
                      {'position': position, 'task': task})
        elif category is not None:
            c.execute('UPDATE todos SET category = :category WHERE position = :position',
                      {'position': position, 'category': category})


def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status=?, date_completed=? WHERE position=?',
                  (2, datetime.datetime.now().isoformat(), position))
