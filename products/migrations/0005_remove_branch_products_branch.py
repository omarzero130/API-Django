# Generated by Django 2.2.6 on 2019-10-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191014_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch_products',
            name='branch',
        ),
    ]