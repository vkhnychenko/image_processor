# Generated by Django 3.0.9 on 2020-08-07 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
    ]