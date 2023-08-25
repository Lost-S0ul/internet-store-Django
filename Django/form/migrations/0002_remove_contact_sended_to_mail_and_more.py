# Generated by Django 4.2.4 on 2023-08-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='sended_to_mail',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='sended_to_mail',
        ),
        migrations.RemoveField(
            model_name='question',
            name='sended_to_mail',
        ),
        migrations.RemoveField(
            model_name='serviceoffer',
            name='sended_to_mail',
        ),
        migrations.AddField(
            model_name='contact',
            name='send_to_mail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='send_to_mail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='send_to_mail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='serviceoffer',
            name='send_to_mail',
            field=models.BooleanField(default=True),
        ),
    ]