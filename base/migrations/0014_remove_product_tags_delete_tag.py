# Generated by Django 5.1.2 on 2024-11-18 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_product_prodimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]