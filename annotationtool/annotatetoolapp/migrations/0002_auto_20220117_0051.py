# Generated by Django 3.1.6 on 2022-01-16 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotatetoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_x', models.FloatField()),
                ('end_x', models.FloatField()),
                ('start_y', models.FloatField()),
                ('end_y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='annotation',
        ),
        migrations.AddField(
            model_name='images',
            name='annotations',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to='app/static/uploads/'),
        ),
        migrations.DeleteModel(
            name='Annot',
        ),
        migrations.AddField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotatetoolapp.images'),
        ),
        migrations.AlterField(
            model_name='images',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotatetoolapp.myuser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]