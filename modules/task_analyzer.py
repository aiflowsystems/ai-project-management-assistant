def analyze_tasks(tasks):
    total_tasks = len(tasks)
    completed_tasks = 0
    in_progress_tasks = 0
    pending_tasks = 0
    high_priority_tasks = 0

    for task in tasks:
        status = task["status"]
        priority = task["priority"]

        if status == "completed":
            completed_tasks += 1
        elif status == "in_progress":
            in_progress_tasks += 1
        elif status == "pending":
            pending_tasks += 1

        if priority == "high":
            high_priority_tasks += 1

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "pending_tasks": pending_tasks,
        "high_priority_tasks": high_priority_tasks
    }