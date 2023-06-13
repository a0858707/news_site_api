from django.contrib import admin
from django.urls import path
from mewsapp import views

urlpatterns = [
    path('', views.index, name='template'),
    path('admin/', admin.site.urls),
]
