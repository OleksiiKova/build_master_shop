# Generated by Django 4.2 on 2024-10-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='sku',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]