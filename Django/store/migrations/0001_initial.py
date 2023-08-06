# Generated by Django 4.2.4 on 2023-08-03 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0003_alter_main_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('render_name', models.CharField(max_length=30)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subdirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('render_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('render_name', models.CharField(max_length=30)),
                ('service_description', models.TextField()),
                ('mini_description', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('render_name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('about_product', models.TextField()),
                ('character', models.TextField()),
                ('additional_images', models.ManyToManyField(related_name='last_slider+', to='images.image')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.catalog')),
                ('images', models.ManyToManyField(related_name='main_slider+', to='images.image')),
                ('subdirectories', models.ManyToManyField(to='store.subdirectory')),
            ],
        ),
        migrations.AddField(
            model_name='catalog',
            name='subdirectories',
            field=models.ManyToManyField(to='store.subdirectory'),
        ),
    ]
