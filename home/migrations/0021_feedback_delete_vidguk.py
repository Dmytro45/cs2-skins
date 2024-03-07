# Generated by Django 4.2.5 on 2024-02-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_vidguk_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('feedback_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Vidguk',
        ),
    ]