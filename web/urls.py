
from django.contrib import admin
from django.urls import path

from crud import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('count/', views.count),
    path('new/', views.new, name='news'),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
]

urlpatterns += staticfiles_urlpatterns()