# Generated by Django 2.2 on 2019-09-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundoonotes',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
