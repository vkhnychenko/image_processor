# Generated by Django 3.0.9 on 2020-08-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200809_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='update_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
