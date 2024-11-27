import tkinter as tk
from tkinter import messagebox

# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task_name = task_entry.get()
    due_date = due_date_entry.get()
    if task_name:
        task = {"name": task_name, "due_date": due_date}
        tasks.append(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)  # Clear the entry field
        due_date_entry.delete(0, tk.END)  # Clear the due date field
    else:
        messagebox.showwarning("Input Error", "Task name cannot be empty!")

# Function to update the Listbox with current tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)  # Clear the Listbox
    for task in tasks:
        due_date = task['due_date'] if task['due_date'] else "No due date"
        task_listbox.insert(tk.END, f"{task['name']} - Due: {due_date}")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the selected task index
        removed_task = tasks.pop(selected_task_index)  # Remove the task from the list
        update_task_listbox()  # Update the Listbox after deletion
        messagebox.showinfo("Task Deleted", f"Task '{removed_task['name']}' deleted successfully!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to initialize the GUI window
def init_gui():
    window = tk.Tk()
    window.title("To-Do List App")
    
    # Set a background color for the window
    window.config(bg="#F0F8FF")
    
    # Create and pack the entry fields for task name and due date
    global task_entry, due_date_entry
    task_label = tk.Label(window, text="Task Name:", font=("Arial", 12), bg="#F0F8FF")
    task_label.pack(pady=10)
    task_entry = tk.Entry(window, width=40, font=("Arial", 12))
    task_entry.pack(pady=5)
    
    due_date_label = tk.Label(window, text="Due Date (optional):", font=("Arial", 12), bg="#F0F8FF")
    due_date_label.pack(pady=10)
    due_date_entry = tk.Entry(window, width=40, font=("Arial", 12))
    due_date_entry.pack(pady=5)
    
    # Create and pack the buttons with a background color
    add_button = tk.Button(window, text="Add Task", width=20, font=("Arial", 12), bg="#90E900", command=add_task)
    add_button.pack(pady=10)
    
    delete_button = tk.Button(window, text="Delete Task", width=20, font=("Arial", 12), bg="#FFCC", command=delete_task)
    delete_button.pack(pady=5)
    
    # Create and pack the Listbox with custom design and background
    global task_listbox
    task_listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12), bg="#F5F5F5", selectmode=tk.SINGLE)
    task_listbox.pack(pady=10)
    
    # Signature at the bottom right corner
    signature_label = tk.Label(window,  font=("Arial", 10, "italic"), bg="#F0F8FF", fg="#555")
    signature_label.place(relx=1.0, rely=1.0, anchor="se", bordermode="outside")

    # Run the Tkinter event loop
    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    init_gui()