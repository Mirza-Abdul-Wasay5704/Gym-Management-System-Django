"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include 

# url dispatching: pages ka change hona 
# entered url comes to firstProject k urls.py per ye isko homeApp kay urls.py per bhejta
# phir wahan se jo bhi match krta wo homeApp kay views.py per jao or jo bhi same name ka function hai run krdo

# manually, for changing django admin page text
admin.site.site_header = "Gym Management Admin"
admin.site.site_title = "Gym Management Admin Portal"
admin.site.index_title = "Welcome to Gym Management Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homeApp.urls'))    # agar ye ' ' path match hota hai to ousko homeApp.urls per bhej do
  
] 
