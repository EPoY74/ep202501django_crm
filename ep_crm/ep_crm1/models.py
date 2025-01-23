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
    name = models.CharField(max_length=100, verbose_name="Имя (название)")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")

    # objects = models.Manager()

    def __str__(self):
        return f"{self.name} | {self.email}"

    class Meta:
        """Изменяю название для отображения в админке
        """
        verbose_name="Клиент"
        verbose_name_plural="Клиенты"

class Deal(models.Model):
    """Модель для хранения данных о сделках

    Args:
        models (django.db.models.Model): Базовый класс для всех моделей в Django
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    status = models.CharField(max_length=50, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        """переопределяю название модели"""
        return f"{self.client} | {self.amount}"


    class Meta:
        """Переопределяю имя модели в админке
        """
        verbose_name="Сделка"
        verbose_name_plural="Сделки"


class Task(models.Model):
    """Модель для храения данных  о заданиях

    Args:
        models (django.db.models.Model): Базовый класс для всех моделей в Django
    """
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Сделка")
    description = models.TextField(verbose_name="Описание")
    due_time = models.DateTimeField(verbose_name="Исполнить до")
    completed = models.BooleanField(default=False, verbose_name="Исполнено")


    def __str__(self):
        """Переопределяю имя модели"""
        return f"{self.deal} | {self.due_time}"


    class Meta:
        """Переопределяю имя модели в админке"""
        verbose_name="Задача"
        verbose_name_plural="Задачи"
