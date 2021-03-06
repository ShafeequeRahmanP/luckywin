# Generated by Django 3.0.8 on 2020-09-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luckyapp', '0013_lottey_result_5pm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stockist_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('agency_name', models.CharField(max_length=20)),
                ('mobile_number_1', models.CharField(max_length=10)),
                ('mobile_number_2', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('existing_stocklist_status', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=1)),
                ('stockist_type', models.CharField(choices=[('S', 'STOCKIST'), ('SS', 'SUB-STOCKIST'), ('SE', 'SELLER')], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='lottey_result_2pm',
            name='first_price',
            field=models.CharField(max_length=10),
        ),
    ]
