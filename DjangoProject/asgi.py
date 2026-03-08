"""
ASGI config for DjangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""
# config/asgi.py
import os

from django.core.asgi import get_asgi_application

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
# Получаем ASGI-приложение
application = get_asgi_application()


"""
Модуль os настраивает переменную окружения
DJANGO_SETTINGS_MODULE, указывающую на файл настроек проекта
● Функция get_asgi_application() импортируется из
django.core.asgi и вызывается для создания ASGIприложения
"""