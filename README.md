# REMOTE SUCCESFULLY BY GIT

# Task Tracker CLI

Task Tracker CLI is a command-line application for managing your tasks efficiently. It allows you to add, update, complete, and view tasks with ease.

## Features

- **Add Tasks**: Add new tasks with optional categories.
- **Update Tasks**: Update the description or category of existing tasks.
- **Complete Tasks**: Mark tasks as completed.
- **View Tasks**: Display the list of tasks with their status.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/task_tracker.git
   cd task_tracker
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Add a Task

To add a new task:

```sh
python todocli.py add "Task description" --category "Category"
```

To update a task:

```sh
python todocli.py update <position> --task "New task description" --category "New category"
```

To complete a task:

```sh
python todocli.py complete <position>
```

To show all tasks:

```sh
python todocli.py show
```
