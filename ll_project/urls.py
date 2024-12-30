"""
URL configuration for ll_project project.

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
# django.contrib.admin 是 Django 的管理员模块，提供了一个管理后台
from django.contrib import admin 
# django.urls.path 是一个用于定义 URL 路径的函数
from django.urls import path, include


"""
urlpatterns 列表定义了 URL 路由配置：
path("admin/", admin.site.urls) 定义了一个 URL 路径，当访问 /admin/ 时，Django 将路由请求到管理员站点。
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('learning_logs.urls')),
]
