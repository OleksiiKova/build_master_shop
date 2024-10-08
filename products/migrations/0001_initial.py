# Generated by Django 4.2 on 2024-10-08 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('sku', models.CharField(max_length=64, unique=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=3, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('additional_attributes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('first_level_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_level_categories', to='products.firstlevelcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('second_level_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_level_categories', to='products.secondlevelcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('color', models.CharField(blank=True, max_length=64, null=True)),
                ('additional_attributes', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('sku', models.CharField(max_length=64, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='second_level_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.secondlevelcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='third_level_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.thirdlevelcategory'),
        ),
    ]
