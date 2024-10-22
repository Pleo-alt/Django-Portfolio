from django.shortcuts import render
from .models import Skill, Project  # Import both models
from django.conf import settings

def home(request):
    skills = Skill.objects.all()  # Fetch all skills from the database
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'index.html', {
        'skills': skills,
        'projects': projects,
        'MEDIA_URL': settings.MEDIA_URL
    })
