# Generated by Django 4.1.5 on 2023-02-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0018_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
