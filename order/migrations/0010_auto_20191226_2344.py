# Generated by Django 2.2.6 on 2019-12-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_orders_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]