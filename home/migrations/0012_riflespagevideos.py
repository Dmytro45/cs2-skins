# Generated by Django 4.2.5 on 2024-02-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_settings_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiflesPageVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=20)),
            ],
        ),
    ]
