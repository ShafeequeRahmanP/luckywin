# Generated by Django 3.0.8 on 2020-09-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luckyapp', '0005_auto_20200909_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottey_result',
            name='second_price',
            field=models.CharField(default=123, max_length=3),
        ),
    ]