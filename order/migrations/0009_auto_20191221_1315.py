# Generated by Django 3.0 on 2019-12-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20191221_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]