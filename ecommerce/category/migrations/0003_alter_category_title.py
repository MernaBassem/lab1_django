# Generated by Django 5.0.1 on 2024-02-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_name_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]