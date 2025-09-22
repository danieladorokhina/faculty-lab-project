from django.shortcuts import render, get_object_or_404
from .models import HomePage, Program, Department, Coordinator

def home_view(request):
    content = HomePage.objects.first()
    return render(request, 'faculty/home.html', {'content': content})

def program_list_view(request):
    programs = Program.objects.all()
    return render(request, 'faculty/program_list.html', {'programs': programs})

def program_detail_view(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': program})

def department_list_view(request):
    departments = Department.objects.all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    
    teachers = department.teachers.all()
    coordinators = {p.coordinator for p in department.programs.all() if p.coordinator}
    
    return render(request, 'faculty/department_detail.html', {
        'department': department,
        'teachers': teachers,
        'coordinators': coordinators
    })