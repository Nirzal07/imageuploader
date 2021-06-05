from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from imageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', views.home, name = 'home'),
    path('register', views.register, name= 'register'),
    path('', views.user_login, name = 'login')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
