# Generated by Django 5.0 on 2024-04-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_rename_seller_inventory_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='seller_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]