# Generated by Django 5.1.2 on 2024-11-21 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_cart_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
