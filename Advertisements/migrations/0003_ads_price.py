# Generated by Django 2.2.3 on 2020-06-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisements', '0002_auto_20200607_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
