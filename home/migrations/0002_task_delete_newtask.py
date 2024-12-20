# Generated by Django 5.1.4 on 2024-12-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='NewTask',
        ),
    ]
