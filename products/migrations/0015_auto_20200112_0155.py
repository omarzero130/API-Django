# Generated by Django 2.2.6 on 2020-01-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200112_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Barcode',
            field=models.CharField(max_length=50),
        ),
    ]