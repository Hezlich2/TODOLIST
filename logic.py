import database

def add_new_task(task):
    if task.strip():
        database.add_task(task)
        return True
    return False

def get_all_tasks():
    return database.get_tasks()

def complete_task(task_id):
    database.mark_done(task_id)

def remove_task(task_id):
    database.delete_task(task_id)
