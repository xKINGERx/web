
from django.contrib import admin
from django.urls import path

from crud import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('count/', views.count),
    path('new/', views.new, name='news')
]
