# Generated by Django 4.1.5 on 2023-02-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('college_name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('enrollment_year', models.IntegerField()),
                ('backlog', models.IntegerField()),
                ('current_year_percentage', models.IntegerField()),
                ('personal_email', models.EmailField(max_length=254)),
                ('college_email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.TextField()),
                ('dob', models.DateField()),
                ('current_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
