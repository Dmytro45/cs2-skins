# Generated by Django 4.2.5 on 2024-02-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_rename_feedback_name_feedback_feedback_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vidguk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vidguk', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]