# Generated by Django 4.2.1 on 2023-05-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type_blog',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
