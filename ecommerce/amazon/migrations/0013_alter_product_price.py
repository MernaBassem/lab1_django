# Generated by Django 5.0.1 on 2024-02-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0012_alter_product_category_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]