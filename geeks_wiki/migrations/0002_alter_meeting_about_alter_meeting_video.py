# Generated by Django 4.2.1 on 2023-05-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geeks_wiki", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="about",
            field=models.TextField(
                blank=True, null=True, verbose_name="Расскажите о себе?"
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="video",
            field=models.URLField(
                blank=True, null=True, verbose_name="Ваш любимый фильм"
            ),
        ),
    ]
