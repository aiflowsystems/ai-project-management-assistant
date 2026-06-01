def calculate_progress(project_summary):
    total_tasks = project_summary["total_tasks"]
    completed_tasks = project_summary["completed_tasks"]

    if total_tasks == 0:
        progress_percentage = 0
    else:
        progress_percentage = round(
            (completed_tasks / total_tasks) * 100,
            1
        )

    return {
        "progress_percentage": progress_percentage
    }