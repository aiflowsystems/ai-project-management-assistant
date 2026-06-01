# AI Project Management Assistant

An AI-powered project management assistant that analyzes tasks, tracks progress, calculates project metrics, and generates structured project reports.

Designed to help teams, freelancers, and small businesses monitor task status, understand project progress, and automate project reporting workflows.

---

## Features

### Task Management

- Read project tasks from CSV files
- Track task status
- Organize tasks by priority
- Support simple project tracking workflows

### Project Analysis

- Count total tasks
- Count completed tasks
- Count in-progress tasks
- Count pending tasks
- Count high-priority tasks

### Progress Tracking

- Calculate project completion percentage
- Track project progress automatically
- Support progress reporting workflows

### Project Reporting

- Generate centralized project reports
- Summarize project status
- Save reports automatically in the outputs folder

---

## Technologies Used

- Python
- CSV Processing
- JSON Configuration
- File Handling
- Pathlib
- Modular Programming
- Project Management Automation
- Business Process Automation

---

## Project Structure

```text
ai-project-management-assistant/

├── main.py
├── config.json
├── tasks.csv
├── README.md
├── .gitignore
│
├── modules/
│   ├── task_analyzer.py
│   ├── progress_tracker.py
│   └── report_generator.py
│
└── outputs/
    └── project_report.txt
```

---

## Workflow

1. Load configuration from `config.json`
2. Read project tasks from `tasks.csv`
3. Analyze task status and priority
4. Calculate project progress
5. Generate a centralized project report
6. Save the report inside the outputs folder

---

## Example Task Input

```csv
task_id,task,status,priority
1,Build API Integration,completed,high
2,Create Dashboard,in_progress,high
3,Write Documentation,pending,medium
4,Deploy Application,completed,high
5,Perform Testing,pending,medium
```

---

## Example Console Output

```text
AI Project Management Assistant
===============================

Tasks loaded: 5
Build API Integration
Create Dashboard
Write Documentation
Deploy Application
Perform Testing

PROJECT SUMMARY
---------------
Total Tasks: 5
Completed Tasks: 2
In Progress Tasks: 1
Pending Tasks: 2
High Priority Tasks: 3

PROJECT PROGRESS
----------------
Progress: 40.0%

Project report generated: outputs\project_report.txt
```

---

## Business Value

Project tracking often involves manually reviewing task lists, calculating progress, and preparing status reports.

This project demonstrates how automation can simplify project management workflows by analyzing task data, calculating progress, and generating structured project reports automatically.

---

## Future Improvements

- Overdue task detection
- Deadline tracking
- AI-generated project recommendations
- Task prioritization scoring
- Dashboard interface
- Email report delivery
- Multi-project support
- Team member assignment tracking
- Scheduled report generation

---

## Author

Adam Zaki

AI Automation Developer

GitHub:
https://github.com/aiflowsystems

Portfolio:
https://aiflowsystems.github.io/portfolio/