# Generated by Django 4.2.5 on 2023-10-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
