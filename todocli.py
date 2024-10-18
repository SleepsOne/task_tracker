import typer
from rich.console import Console
from rich.table import Table
import database as db
from model import Todo


console = Console()

app = typer.Typer()


@app.command(short_help="adds a item")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo_add = Todo(task, category)
    db.insert_todo(todo_add)

    db.conn.commit()
    show()


@app.command(short_help="delete an item pass by position")
def delete(postition: int):
    typer.echo(f"deleting {postition}")
    db.delete_todo(postition-1)  # position in UI start with 1

    show()

    db.conn.commit()


@app.command()
def update(position: int, task: str = typer.Option(None, help="The task description"), category: str = typer.Option(None, help="The task category")):
    typer.echo(f"updating {position}")
    db.update_todo(position-1, task, category)
    show()
    db.conn.commit()
    show()


@app.command(short_help="mark as complete a task")
def complete(position: int):
    typer.echo(f"completed {position}")
    db.complete_todo(position-1)
    db.conn.commit()
    show()


@app.command(short_help="show all todos as list")
def show():

    tasks = db.getall_todos()
    console.print("[bold magenta]TODOS[/bold magenta]", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red',
                  'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for task in tasks:
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else "❌"
        table.add_row(str(task.position + 1), task.task,
                      f'[{c}]{task.category}[/{c}]', is_done_str)

    console.print(table)


if __name__ == "__main__":
    app()
