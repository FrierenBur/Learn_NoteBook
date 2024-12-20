"""
ASGI config for ll_project project.
ASGI（异步服务器网关接口）配置文件
It exposes the ASGI callable as a module-level variable named ``application``.
并且这个文件将 ASGI callable 暴露为一个名为 application 的模块级变量
"""

import os

from django.core.asgi import get_asgi_application
#* 设置环境变量DJANGO_SETTINGS_MODULE的默认值为ll_project.settings，也就是ll_project项目的settings.py文件
#* 修改此处代码可以使用其他配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ll_project.settings")

#* 这行代码调用了 get_asgi_application 函数，并将其返回值赋给变量 application。
#* 这个 application 变量就是 ASGI callable，ASGI 服务器将使用它来与 Django 应用进行通信。
application = get_asgi_application()
