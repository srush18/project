# Generated by Django 4.1.7 on 2023-04-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='backlog',
        ),
    ]
