# Generated by Django 5.0 on 2024-03-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_cart_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_order',
            name='user_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user_order',
            name='user_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
