# Generated by Django 3.0.7 on 2021-03-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0011_auto_20210303_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pickup_date',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_date',
            field=models.DateField(max_length=30),
        ),
    ]
