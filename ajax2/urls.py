"""ajax2 URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path ,include
from django.views.decorators.csrf import csrf_exempt
from ajaxapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('save/',views.save,name='save'),
    path('delete/',views.delete,name='delete'),
    path('edit/',views.edit,name='edit'),
    path('search/',csrf_exempt(views.search),name='search'),
    path('login/',views.Login,name='login'),
    path('profile/',views.ProfileView.as_view(),name='Profile'),
    path('accounts/',include('allauth.urls')),
    path('verification/', include('verify_email.urls')),
    path('reg/',views.RegForm,name='reg'),	
    path('logout/',views.logoutuser,name='logout'),	

]
