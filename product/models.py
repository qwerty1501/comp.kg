from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/product')
    name = models.CharField(verbose_name='Название продукта', max_length=50)
    discriptions = models.TextField(verbose_name='Описание')
    price = models.CharField(verbose_name='Цена', max_length=20)
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return self.name
    

class Image(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/dop_images')
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Доп_Фотографии'
        
    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    images = models.ForeignKey(Image, verbose_name="Фотография", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.images}'