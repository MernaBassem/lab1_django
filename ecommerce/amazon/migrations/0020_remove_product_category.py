# Generated by Django 5.0.1 on 2024-02-07 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0019_remove_product_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
