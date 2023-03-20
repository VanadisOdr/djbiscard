from django.contrib import admin
from django.urls import path
from hello.views import home


urlpatterns = [
    path('work/', admin.site.urls),
    path('', home)
]