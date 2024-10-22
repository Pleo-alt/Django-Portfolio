from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),  # Changed '' to 'index/' for a unique path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
