# Generated by Django 3.0.7 on 2021-03-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0010_auto_20210303_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pickup_date',
            field=models.DateTimeField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_date',
            field=models.DateTimeField(max_length=30),
        ),
    ]
