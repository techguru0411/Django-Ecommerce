# Generated by Django 2.2.4 on 2019-10-01 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20191001_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]
