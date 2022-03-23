# Generated by Django 3.1.6 on 2022-01-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_automobiles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Automobiles',
        ),
        migrations.AddField(
            model_name='todo',
            name='Automobiles',
            field=models.CharField(choices=[('Bus', 'Bus'), ('Car', 'Car'), ('Auto', 'Auto'), ('Bike', 'Bike')], default='Bus', max_length=100),
        ),
    ]