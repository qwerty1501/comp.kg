# Generated by Django 3.2.9 on 2022-09-20 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220920_1132'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
