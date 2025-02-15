"""
URL configuration for VerifyPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
import IDGenie
from django.conf.urls.static import static
from django.conf.urls import include



urlpatterns = [
    # This is the url that helps take the user to the landing page
    path('', include('IDGenie.urls')),
    
    path('admin/', admin.site.urls),
    
    # CKEditor settings
CKEDITOR_UPLOAD_PATH = "uploads/"  # Path where uploaded images and files will be stored
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',  # Or use another toolbar option like 'Basic', 'Standard', etc.
        'height': 300,  # Set the height of the CKEditor
        'width': '100%',  # Set the width to 100% of the container
        'filebrowserUploadUrl': '/ckeditor/upload/',  # URL for file uploads (if using 'ckeditor_uploader')
        'filebrowserImageUploadUrl': '/ckeditor/upload/',  # URL for image uploads
    }
}

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
