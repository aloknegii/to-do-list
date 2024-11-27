
# To-Do List App

A simple and interactive **To-Do List Application** built using Python's `tkinter` library. This app allows users to add tasks, assign optional due dates, and manage their to-do list efficiently.

---

## Features

- **Add Tasks**: Quickly add tasks with an optional due date.
- **View Tasks**: See all tasks in an easy-to-read list format.
- **Delete Tasks**: Remove tasks from the list with a single click.
- **Interactive GUI**: User-friendly interface with labeled fields and buttons.
- **Custom Styling**: Aesthetic design using colors and fonts for a pleasant experience.

---

## Project Structure

```plaintext
.
├── main.py              # Main Python file containing the application logic
├── README.md            # Documentation for the project
└── LICENSE              # Optional license file
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your system.
- No additional libraries required (only uses the built-in `tkinter` module).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-list-app
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## How to Use

1. **Add a Task**:
   - Enter the task name in the "Task Name" field.
   - Optionally, enter a due date in the "Due Date" field.
   - Click **Add Task** to save the task to the list.

2. **View Tasks**:
   - All added tasks appear in the central list with their due dates.

3. **Delete a Task**:
   - Select a task from the list.
   - Click **Delete Task** to remove it.

---



---

## Features in Detail

### User Input
- **Task Name**: A required field for naming the task.
- **Due Date**: An optional field for specifying deadlines.

### Validation
- Warns users if they attempt to add a task without a name.
- Ensures proper selection for deletion operations.

### Notifications
- Displays success or error messages using `messagebox`.

---

## Future Improvements

- **Task Persistence**:
  - Save tasks to a file or database for persistence across sessions.
- **Enhanced Features**:
  - Add priorities to tasks.
  - Implement a search or filter functionality.
- **UI Enhancements**:
  - Integrate modern GUI elements using frameworks like `ttk` or `PyQt`.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Created with Python's built-in `tkinter` library.
- Designed for simple task management with a focus on usability.

---

