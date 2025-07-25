from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello from Django on AWS App Runner!</h1><p>Your Django application is running successfully.</p>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]