# Generated by Django 4.2.1 on 2023-05-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ваше имя?')),
                ('age', models.PositiveIntegerField(default=18, verbose_name='Ваш возраст?')),
                ('image', models.ImageField(upload_to='', verbose_name='Добавьте фотку')),
                ('about', models.TextField(verbose_name='Расскажите о себе?')),
                ('number_phone', models.CharField(max_length=13, verbose_name='Ваш номер телефона')),
                ('video', models.URLField(verbose_name='Ваш любимый фильм')),
                ('history_love', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет'), ('Никогда', 'Никогда')], max_length=100, verbose_name='Были ли вы в отношениях?')),
                ('purpose_of_dating', models.CharField(choices=[('Для дружбы', 'Для дружбы'), ('Для отношений', 'Для отношений'), ('Для брака', 'Для брака')], max_length=100, verbose_name='Цель знакомства?')),
            ],
        ),
    ]
