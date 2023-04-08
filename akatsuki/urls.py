"""akatsuki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from peace import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('template1/',views.template1),
    path('footer1/',views.footer1),
    path('model_relations/',views.model_relation),
    
    path('form1/',views.form1),
    path('delete/<int:myid>',views.deleteform, name='formdelete'),
    path("edit/<int:myid>", views.editform, name="formedit"),
    path("updated/<int:myid>", views.updateform, name="formupdate"),
    path('form1list/',views.form1list,name='formlist'),
    
    path('taka/',include('taka.urls')),
    
    path('konaha/',include('konaha.urls')),
    
    path('auth/',include('authenticate.urls')),
    
]