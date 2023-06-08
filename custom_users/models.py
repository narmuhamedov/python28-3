from django.db import models
from django.contrib.auth.models import User

GENDER = (("М", "M"), ("Ж", "Ж"))


class CustomUsers(User):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    phone_number = models.CharField(max_length=15, default="+996777888999")
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=100, choices=GENDER)
    work = models.TextField(blank=True, default="Я работаю в")

    def __str__(self):
        return self.username
