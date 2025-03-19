import tkinter as tk
from tkinter import messagebox
import logic

def refresh_list():
    task_list.delete(0, tk.END)
    for task in logic.get_all_tasks():
        task_list.insert(tk.END, f"{task[0]}: {task[1]} - {task[2]}")

def add_task():
    task = task_entry.get()
    if logic.add_new_task(task):
        task_entry.delete(0, tk.END)
        refresh_list()
    else:
        messagebox.showerror("Ошибка", "Нельзя добавить пустую задачу!")

def complete_task():
    try:
        task_id = int(task_list.get(tk.ACTIVE).split(":")[0])
        logic.complete_task(task_id)
        refresh_list()
    except:
        messagebox.showerror("Ошибка", "Выберите задачу!")

def delete_task():
    try:
        task_id = int(task_list.get(tk.ACTIVE).split(":")[0])
        logic.remove_task(task_id)
        refresh_list()
    except:
        messagebox.showerror("Ошибка", "Выберите задачу!")

# Окно приложения
root = tk.Tk()
root.title("Менеджер задач")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Добавить", command=add_task)
add_button.pack(side=tk.LEFT)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

done_button = tk.Button(btn_frame, text="Отметить выполненной", command=complete_task)
done_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(btn_frame, text="Удалить", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

refresh_list()

root.mainloop()

def start_app():
    root.mainloop()

