# Generated by Django 5.0 on 2023-12-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_remove_category_product_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="products.category",
                verbose_name="Категории",
            ),
        ),
    ]
