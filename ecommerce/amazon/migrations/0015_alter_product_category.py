# Generated by Django 5.0.1 on 2024-02-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0014_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Default Category', max_length=255),
        ),
    ]
