# Generated by Django 5.1.2 on 2024-11-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]