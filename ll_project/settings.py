from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-67y8=(!-nclq2^304gy7mgql4*m^(0f9d2un5f^71#csh30%eo"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS 是一个允许的主机名列表，生产环境中应配置实际的域名或 IP 地址。
ALLOWED_HOSTS = []


# Application definition
# INSTALLED_APPS 列表定义了项目中安装和启用的应用程序，这里列出了一些 Django 内置的应用程序
# 如管理网站、认证系统、会话管理、消息框架和静态文件处理。
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# MIDDLEWARE 列表定义了项目中使用的中间件，每个中间件是一个在请求和响应过程中执行特定功能的类。
# 这里列出了一些常用的中间件，如安全中间件、会话中间件、CSRF 防护中间件、认证中间件等。
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ROOT_URLCONF 指定了根 URL 配置模块，即项目的 URL 配置文件
ROOT_URLCONF = "ll_project.urls"

"""
TEMPLATES 配置了 Django 的模板引擎：
BACKEND 指定模板引擎的后端。
DIRS 指定模板文件目录。
APP_DIRS 设置为 True，表示自动加载应用程序目录中的模板。
OPTIONS 包括一些上下文处理器，它们在渲染模板时提供额外的上下文数据。
"""
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION 指定 WSGI 应用程序的路径，用于部署项目
WSGI_APPLICATION = "ll_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
"""
DATABASES 配置了数据库的连接信息：
ENGINE 指定数据库引擎，这里使用的是 SQLite。
NAME 指定数据库文件的路径。
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS 列表定义了密码验证器，用于加强密码的安全性
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
"""
国际化和本地化设置：
LANGUAGE_CODE 设置语言代码。
TIME_ZONE 设置时区。
USE_I18N 启用国际化。
USE_TZ 启用时区支持。
"""

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL 设置了静态文件的 URL 前缀
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD 设置了默认的主键字段类型
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
