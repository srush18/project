# Generated by Django 4.1.7 on 2023-04-11 16:58

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
                ('student_image', models.ImageField(upload_to='pictures')),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_code')),
                ('name', models.CharField(max_length=20)),
                ('personal_email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('current_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('college_name', models.CharField(max_length=100)),
                ('enrollment_year', models.IntegerField()),
                ('course', models.CharField(max_length=20)),
                ('branch', models.CharField(default='', max_length=20)),
                ('roll_no', models.IntegerField()),
                ('college_email', models.EmailField(max_length=254)),
                ('current_cgpa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('backlog', models.CharField(max_length=20)),
            ],
        ),
    ]
