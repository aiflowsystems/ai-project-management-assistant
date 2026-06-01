def generate_project_report(project_summary, project_progress):
    report = f"""AI Project Management Assistant Report

Project Summary
===============

Total Tasks: {project_summary['total_tasks']}
Completed Tasks: {project_summary['completed_tasks']}
In Progress Tasks: {project_summary['in_progress_tasks']}
Pending Tasks: {project_summary['pending_tasks']}
High Priority Tasks: {project_summary['high_priority_tasks']}

Project Progress
================

Progress: {project_progress['progress_percentage']}%
"""

    return report