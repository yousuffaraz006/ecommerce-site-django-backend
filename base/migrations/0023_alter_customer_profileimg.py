# Generated by Django 5.1.2 on 2024-11-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_customer_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profileimg',
            field=models.ImageField(blank=True, default='images/user.png', null=True, upload_to='base/images/'),
        ),
    ]
