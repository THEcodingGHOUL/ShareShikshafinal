"""shareshiksha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', views.home_view),
    path('',views.home_view),
    path('admin_login/', views.admin_login),
    path('contact/' ,views.contact),
    path('member_login/', views.member_login),
    path('grievance/',views.grievances_form),
    path('addgrievance/',views.addgrievance),
    path('currgrievance/',views.currgrievance),
    path('memberpage/',views.memberpage),
    path('adminpage/',views.adminpage),
    path('admin_login/adminpage/updateresource/',views.updateresource),
]
