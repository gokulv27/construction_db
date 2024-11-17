from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    # Home view, which could show a message or redirect
    return render(request, 'project/project.html', {'view': 'home'})

def project_list(request):
    # List all projects
    projects = Project.objects.all()   
    return render(request, 'project/project.html', {'projects': projects, 'view': 'project_list'})

def project_detail(request, pk):
    # Show details of a specific project
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project.html', {'projects': projects, 'view': 'project_detail'})
    