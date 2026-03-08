"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

# Получаем WSGI-приложение
application = get_wsgi_application()

"""Настройка сервера
Инициализация проекта
Развертывание

Модуль os настраивает переменную окружения
DJANGO_SETTINGS_MODULE, указывающую на файл настроек проекта
● Функция get_wsgi_application() импортируется из
django.core.wsgi и вызывается для создания WSGIприложения"""
