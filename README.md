# Faculty Lab Project

This is a Django project for my lab work.  
It has one app **faculty** with models for Department, Teacher and Program.  

## How to run
```bash
git clone https://github.com/your-username/faculty-lab-project.git
cd faculty-lab-project
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install django
python manage.py migrate
python manage.py runserver
