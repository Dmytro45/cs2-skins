# Generated by Django 4.2.5 on 2024-02-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_riflespagephotos_delete_riflespagevideos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riflespagephotos',
            name='picture',
            field=models.ImageField(null=True, upload_to='rifles_page_photos'),
        ),
    ]
