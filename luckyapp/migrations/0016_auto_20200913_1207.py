# Generated by Django 3.0.8 on 2020-09-13 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luckyapp', '0015_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockist_model',
            name='existing_stocklist_status',
        ),
        migrations.RemoveField(
            model_name='stockist_model',
            name='stockist_type',
        ),
    ]
