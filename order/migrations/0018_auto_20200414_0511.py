# Generated by Django 3.0 on 2020-04-14 03:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200414_0511'),
        ('order', '0017_auto_20200410_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='features',
            field=models.ManyToManyField(default=None, to='products.features'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 3, 11, 27, 436005, tzinfo=utc)),
        ),
    ]