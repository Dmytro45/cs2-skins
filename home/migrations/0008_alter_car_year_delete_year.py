# Generated by Django 4.2.5 on 2023-10-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_model_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
