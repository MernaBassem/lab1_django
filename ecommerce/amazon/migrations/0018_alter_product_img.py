# Generated by Django 5.0.1 on 2024-02-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0017_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='', upload_to='amazon/images/'),
        ),
    ]
