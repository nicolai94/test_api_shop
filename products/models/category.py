# from django.db import models
#
#
# class Category(models.Model):
#     name: str = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     image = models.ImageField(upload_to="categories/%Y/%m/%d", blank=False)
#
#     class Meta:
#         ordering = ("name",)
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"
#
#     def __str__(self) -> str:
#         return self.name
