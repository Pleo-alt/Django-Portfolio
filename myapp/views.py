from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Skill, Project, List_Category
from .forms import ContactForm
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {
        'skills': skills,
        'projects': projects,
        'MEDIA_URL': settings.MEDIA_URL
    })

# Fetch categories for a selected project dynamically (AJAX request)
def get_categories(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    categories = List_Category.objects.filter(project=project)
    category_data = [{
        'name': category.name,
        'image': category.image.url,
        'description': category.description,
        'github_url': category.github_url,
    } for category in categories]
    
    return JsonResponse(category_data, safe=False)

# Contact form view
def contact(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    categories = List_Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"New Contact: {subject}",
                    message=f"Message from {name} ({email}):\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
                logger.info(f"Email sent successfully to {settings.EMAIL_HOST_USER}")
            except Exception as e:
                messages.error(request, "An error occurred while sending your message.")
                logger.error(f"Error sending email: {e}")

            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'skills': skills,
        'projects': projects,
        'categories': categories,
        'form': form,
        'MEDIA_URL': settings.MEDIA_URL
    })

# Project detail view (optional, based on modal usage)
def project_detail(request, project_id):
    # Get the project by its ID
    project = Project.objects.get(id=project_id)
    # Pass the project data to the index template
    return render(request, 'index.html', {
        'project': project,
        'MEDIA_URL': settings.MEDIA_URL
    })
