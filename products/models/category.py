from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name: str = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name
