# Generated by Django 3.0.7 on 2021-03-03 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0007_auto_20210302_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pickup_date',
            field=models.DateField(default=datetime.datetime.now, max_length=8),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_date',
            field=models.DateField(max_length=8),
        ),
    ]
