# Generated by Django 5.1.2 on 2024-11-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, default='Your order has been placed successfully!', max_length=1000, null=True),
        ),
    ]