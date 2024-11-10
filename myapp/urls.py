from django.urls import path
from .views import home, contact, get_categories,project_detail  # Import the views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-categories/<int:project_id>/', views.get_categories, name='get_categories'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
