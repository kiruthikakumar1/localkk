"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hubapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hh/',views.homes),
    path('',views.main),
    path('i/',views.persons),
    path('i/perdet/<int:id>',views.perdetails,name='perdetails'),
    path('user/',views.get_name),
    path('addperson/',views.addperson,name='addperson'),
    path('addpersoncreate/',views.addpersoncreate,name='addpersoncreate'),
    path('i/perdet/<int:id>/deleteperson/', views.deleteperson, name='deleteperson'),
    path('i/perdet/<int:id>/update/', views.update, name='update'),
    path('test/',views.test,name='test'),
    path('i/perdet/<int:id>/update/updateperson/', views.updateperson, name='updateperson'),
    path('ffn/',views.ffn,name='ffn'),
    path('fln/',views.fln,name='fln'),
    path('fc/',views.fc,name='fc'),
]
