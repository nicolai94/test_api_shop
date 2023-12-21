from django.db import models

from common.models.mixins import CreatUpdateTimeMixin


class Product(CreatUpdateTimeMixin):
    name: str = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Количество")
    category = models.ManyToManyField(
        "Category",
        blank=True,
        related_name="products",
        verbose_name="Категории"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=False)

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товаров"
        ordering = ("-id",)

    def __str__(self) -> str:
        return f"Image: {self.product.name}"
