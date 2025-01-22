"""
    Автор: Евгений Петров
    Цель: Написать CRM для изучения Django
    Тип проекта: Учебный
    Начало: 22 января 2025 года
    Почта: epoy74@gmail.com
"""


from django.db import models

# Create your models here.

class Client(models.Model):
    """Модель для хранения данных о клиентах

    Args:
        models (django.db.models.Model): Базовый класс для всех моделей в Django
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TimeField()


class Deal(models.Model):
    """Модель для хранения данных о сделках

    Args:
        models (django.db.models.Model): Базовый класс для всех моделей в Django
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    """Модель для храения данных  о заданиях

    Args:
        models (django.db.models.Model): Базовый класс для всех моделей в Django
    """
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    description = models.TextField()
    due_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
