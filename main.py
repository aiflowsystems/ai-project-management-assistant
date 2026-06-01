import csv
import json
from pathlib import Path
from modules.task_analyzer import analyze_tasks
from modules.progress_tracker import calculate_progress
from modules.report_generator import generate_project_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]

Path(output_folder).mkdir(exist_ok=True)

tasks = []

with open("tasks.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)

project_summary = analyze_tasks(tasks)
project_progress = calculate_progress(project_summary)
project_report = generate_project_report(
    project_summary,
    project_progress
)

print("AI Project Management Assistant")
print("===============================")
print()

print(f"Tasks loaded: {len(tasks)}")

for task in tasks:
    print(task["task"])

print()
print("PROJECT SUMMARY")
print("---------------")
print(f"Total Tasks: {project_summary['total_tasks']}")
print(f"Completed Tasks: {project_summary['completed_tasks']}")
print(f"In Progress Tasks: {project_summary['in_progress_tasks']}")
print(f"Pending Tasks: {project_summary['pending_tasks']}")
print(f"High Priority Tasks: {project_summary['high_priority_tasks']}")

print()
print("PROJECT PROGRESS")
print("----------------")
print(f"Progress: {project_progress['progress_percentage']}%")

report_file = (
    Path(output_folder)
    / config["project_report_file"]
)

with open(report_file, "w", encoding="utf-8") as file:
    file.write(project_report)

print()
print(f"Project report generated: {report_file}")
