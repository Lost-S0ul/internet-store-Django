# Generated by Django 4.2.4 on 2023-08-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_slider',
            name='image',
            field=models.ImageField(upload_to='static/images/images/'),
        ),
    ]
