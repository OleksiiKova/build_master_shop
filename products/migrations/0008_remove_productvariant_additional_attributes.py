# Generated by Django 4.2 on 2024-11-10 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='additional_attributes',
        ),
    ]