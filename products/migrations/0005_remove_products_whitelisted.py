# Generated by Django 3.0.8 on 2020-07-21 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_whitelisted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='whitelisted',
        ),
    ]