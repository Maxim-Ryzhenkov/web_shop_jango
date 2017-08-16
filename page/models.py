from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    class Meta:
        ordering = ['-price', 'name']
        unique_together = ('category', 'name', 'price')
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s += " (нет в наличии)"
        return s

    def save(self, *args, **kwargs):
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Good, self).delete(*args, **kwargs)

    def get_in_stock(self):
        return '+' if self.in_stock else ''

    def get_absolute_url(self):
        pass


class BlogArticle(models.Model):
    title = models.CharField(unique_for_month='pubdate', max_length=100)
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
