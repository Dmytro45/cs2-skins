# Generated by Django 4.2.5 on 2023-10-08 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.color'),
        ),
    ]
