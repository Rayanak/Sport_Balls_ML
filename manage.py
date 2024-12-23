"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(): # Определение функции main для выполнения административных задач
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoModel.settings')
    try:
        from django.core.management import execute_from_command_line # Импорт функции выполнения командной строки из модуля управления Django
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__': # Проверка, был ли скрипт запущен напрямую
    main() # Вызов функции main
