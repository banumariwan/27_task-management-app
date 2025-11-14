 📝ToDo App (Task Management App)

A full-featured Task Management App built with Django.  
This app allows users to add tasks with categories, filter tasks by status, paginate the list, and highlight upcoming deadlines.

## Features

- Add tasks with title, category, deadline, and status (completed/pending)
- Filter tasks by status
- Pagination (5 tasks per page)
- Task counts per category (using annotation)
- Highlight upcoming and overdue tasks
- Clean base model inheritance for timestamps
- Icon-based visual indicators for task status

## Installation

1. Clone the repository:

```bash
git clone https://github.com/banumariwan/todo-app.git
cd todo-app
Create a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open in browser:

http://127.0.0.1:8000/tasks/

Future Features
User authentication (each user sees their own tasks)

Edit and delete tasks

Mark tasks as completed directly from the list

Dashboard with progress charts

yaml
Copy code

---

## 2️⃣ Add & Commit README

```bash
git add README.md
git commit -m "Add README for ToDo App"
git push
