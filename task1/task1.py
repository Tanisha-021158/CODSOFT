import tkinter as tk
from tkinter import messagebox
import json
import os

file = "to_do.json"

# Load tasks
def load_tasks():
    if not os.path.exists(file) or os.stat(file).st_size == 0:
        return []
    with open(file, "r") as f:
        return json.load(f)

# Save tasks
def save_tasks(tasks):
    with open(file, "w") as f:
        json.dump(tasks, f, indent=4)

# Update task listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔ " if task["done"] else "⏳ "
        task_listbox.insert(tk.END, status + task["task"])

# Add new task
def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        task_entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

# Mark task as done
def mark_done():
    selected = task_listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]["done"] = True
        update_listbox()
    else:
        messagebox.showinfo("No Selection", "Select a task to mark as done.")

# Delete a task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        idx = selected[0]
        del tasks[idx]
        update_listbox()
    else:
        messagebox.showinfo("No Selection", "Select a task to delete.")

# Save on close
def on_close():
    save_tasks(tasks)
    root.destroy()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🌈 Colorful To-Do List")
root.geometry("400x500")
root.config(bg="#f0f4f7")

tasks = load_tasks()

title = tk.Label(root, text="My To-Do List 📝", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#2c3e50")
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 12), width=28)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="➕ Add Task", font=("Helvetica", 12), bg="#27ae60", fg="white", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=12, selectbackground="#74b9ff", activestyle="none")
task_listbox.pack(pady=10)

done_button = tk.Button(root, text="✔ Mark as Done", font=("Helvetica", 12), bg="#2980b9", fg="white", command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="🗑 Delete Task", font=("Helvetica", 12), bg="#c0392b", fg="white", command=delete_task)
delete_button.pack(pady=5)

update_listbox()
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
