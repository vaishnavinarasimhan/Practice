# Generated by Django 3.1.6 on 2022-01-15 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20220115_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobiles',
            name='Automobiles',
        ),
    ]