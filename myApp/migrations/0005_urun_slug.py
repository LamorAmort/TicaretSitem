# Generated by Django 3.2.16 on 2022-10-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20221012_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
