# Generated by Django 4.2 on 2024-11-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_productvariant_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=2, null=True),
        ),
    ]
