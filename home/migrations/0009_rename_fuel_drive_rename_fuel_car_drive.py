# Generated by Django 4.2.5 on 2023-10-13 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_car_year_delete_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fuel',
            new_name='Drive',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='fuel',
            new_name='drive',
        ),
    ]
