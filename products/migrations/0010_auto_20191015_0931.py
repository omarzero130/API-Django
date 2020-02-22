# Generated by Django 2.2.6 on 2019-10-15 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20191014_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='prev_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.AddField(
            model_name='branch_products',
            name='prev_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch_products',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='branch_products',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='br', to='products.branch'),
        ),
    ]