# Generated by Django 3.0.8 on 2020-09-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luckyapp', '0020_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date_Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entered', models.DateField()),
            ],
        ),
    ]
