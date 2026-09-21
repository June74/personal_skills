"""Intentionally flawed synthetic fixture for evaluations; not production code."""
def complete_task(tasks, task_id, actor_id):
    task = tasks[task_id]
    task["done"] = True
    return task

def completion_ratio(done, total):
    return done / total
