# Generated by Django 4.1.5 on 2023-01-16 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_tatal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tatal',
            new_name='tatol',
        ),
    ]