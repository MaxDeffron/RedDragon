from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
#Получение прямых URl

from django.db.models import CharField
from django.urls import reverse

#Первичная таблица категорий

class Category(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название категории')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name

    # Тут надо написать название шаблона, куда будет выводиться инфа

    def get_absolute_url (self):
        return reverse('card:product_list_by_category',
                      args=[self.slug])

#Первичная таблица Наименование графического процессора

class Processor(models.Model):
    name = models.CharField (max_length=150,
                            db_index=True,
                            verbose_name='Название графического процессора')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Графический процессор'
        verbose_name_plural = 'Графический процессор'

    def __str__(self):
        return self.name

#Первичная таблица производителей

class Manufacturer(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название производителя')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'

    def __str__(self):
        return self.name

#Первичная таблица типов памяти

class Memory(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название типа памяти')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип памяти'
        verbose_name_plural = 'Тип памяти'

    def __str__(self):
        return self.name

#Первичная таблица видеоразъемов
class Сonnector(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название типа видеоразъема')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Видеоразъем'
        verbose_name_plural = 'Видеоразъем'

    def __str__(self):
        return self.name

#Первичная таблица типов питания
class Power(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название типа кабеля питания')

    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Кабель питания'
        verbose_name_plural = 'Кабель питания'

    def __str__(self):
        return self.name

class Product(models.Model):

#Категории из таблицы Category
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
#Название видеокарты
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='Видеокарта')
#Процессор
    processor = models.ForeignKey(Processor, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Графический процессор')
#Хешрейт
    hashrate = models.DecimalField(max_digits=5,
                                   decimal_places=2,
                                   verbose_name='Хешрейт',null=True)
#Цена
    price = models.DecimalField(max_digits=15,
                                decimal_places=2,
                                verbose_name='Цена', null=True)
#Вес
    weight = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 verbose_name='Вес', null=True)
#LHR
    lhr = models.BooleanField(default=True,
                               verbose_name='LHR')

#Производитель
    manufacturer = models.ForeignKey(Manufacturer, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Производитель графического процессора')

#Тип памяти
    memory = models.ForeignKey(Memory, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Тип памяти')

#Объем видеопамяти
    videomemory = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 verbose_name='Объем видеопамяти', null=True)
#Частота видеопроцессора
    frequency = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 verbose_name='Частота видеопроцессора', null=True)
#Колличество вентиляторов
    cooler = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                verbose_name='Колличество вентиляторов', null=True)

#Фото
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                          blank=True,
                          verbose_name='Фото')

#Описание
    description = models.TextField(blank=True,
                                   verbose_name='Описание')

#Энергопотребление
    power = models.DecimalField(max_digits=5,
                             decimal_places=2,
                             verbose_name='Энергопотребление', null=True)


#Видеоразъем
    connector = models.ForeignKey(Сonnector, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Видеоразъем')


#Питание
    power = models.ForeignKey(Power, related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Кабеля питания')

#Габариты
    length = models.DecimalField(max_digits=5,
                            decimal_places=2,
                            verbose_name='Длина',null=True)
    height = models.DecimalField(max_digits=5,
                            decimal_places=2,
                            verbose_name='Высота',null=True)
    width = models.DecimalField(max_digits=5,
                            decimal_places=2,
                            verbose_name='Ширина',null=True)

#Цена у конкурентов
    price_2 = models.DecimalField(max_digits=15,
                                decimal_places=2,
                                verbose_name='Цена у конкурентов',null=True)
#Акция
    action = models.BooleanField(default=True,
                               verbose_name='Акция')

#Новинки
    new = models.BooleanField(default=True,
                               verbose_name='Новая')

    slug = models.CharField(max_length=200,
                            db_index=True)

    available = models.BooleanField(default=True,
                                    verbose_name='Наличие')

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
>>>>>>> models_db
