"""bus URL Configuration

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
from django.urls import path
from .views import Sub, Sub1
from  content.views import new, create, create_comment, detail, home ,comment_create_ajax

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Sub.as_view()),
    path('samchung/', Sub1.as_view()),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('detail/<int:post_id>', detail, name = 'detail'),
    path('samchung/create_comment/<int:post_id>', create_comment, name='samchung/create_comment/'),
    path('home/',home , name ='home'),
    path('comment/create',comment_create_ajax, name="comment_create_ajax")

]