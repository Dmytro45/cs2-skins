# Generated by Django 4.2.5 on 2024-01-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_fuel_drive_rename_fuel_car_drive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
