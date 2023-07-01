from django.contrib import admin
from django.urls import path
from hello.views import home
from hello import views

urlpatterns = [
    path('work/', admin.site.urls),
    path('', home),
    path('upload/', views.upload_file, name='upload_file')
]