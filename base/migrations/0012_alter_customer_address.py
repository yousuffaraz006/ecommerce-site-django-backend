# Generated by Django 5.1.2 on 2024-11-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
