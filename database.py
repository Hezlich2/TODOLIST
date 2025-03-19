import sqlite3

DB_NAME = "todo.db"

def connect_db():
    """Создание базы данных и таблицы задач"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task TEXT NOT NULL,
                        status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_task(task):
    """Добавление новой задачи"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "не выполнено"))
    conn.commit()
    conn.close()

def get_tasks():
    """Получение списка задач"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_done(task_id):
    """Отметить задачу как выполненную"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'выполнено' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Удаление задачи"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
