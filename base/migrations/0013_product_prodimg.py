# Generated by Django 5.1.2 on 2024-11-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prodimg',
            field=models.ImageField(blank=True, null=True, upload_to='base/images/'),
        ),
    ]
