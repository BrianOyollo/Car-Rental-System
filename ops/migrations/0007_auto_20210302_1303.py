# Generated by Django 3.0.7 on 2021-03-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0006_auto_20210302_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleprofile',
            name='best_image',
            field=models.ImageField(default='no-image1.jpg', upload_to='vehicles'),
        ),
        migrations.AlterField(
            model_name='vehicleprofile',
            name='image',
            field=models.ImageField(default='no-image2.png', upload_to='vehicles'),
        ),
    ]
