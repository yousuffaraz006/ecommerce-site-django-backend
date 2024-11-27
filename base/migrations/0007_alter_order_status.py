# Generated by Django 5.1.2 on 2024-11-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
    ]
