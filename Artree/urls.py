"""
URL configuration for Artree project.

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
from django.http import HttpResponse
from halaman_awal.admin import halaman_awal_site

from halaman_awal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeadmin/', halaman_awal_site.urls),
    path('', views.index),
]

# admin.site.index_title = "LitGo Admin Dashboard"
# admin.site.site_header = "LitGo Admin"
# admin.site.site_title =  "Admin"