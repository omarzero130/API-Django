# Generated by Django 2.2.6 on 2020-02-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200206_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cost',
            field=models.FloatField(default=100.0),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(default=100.0),
        ),
    ]