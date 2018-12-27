from django.db import models

class MainCat(models.Model):
    number_pp = models.IntegerField(default=1, blank=True, null=True)
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    discount = models.CharField(max_length=255, default='', blank=True, null=True)
    info = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return 'Главная категория %s' % self.name

    class Meta:
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"


class SubCat(models.Model):
    main_cat = models.ForeignKey(MainCat, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    number_pp = models.IntegerField(default=1, blank=True, null=True)
    block = models.IntegerField(default=0, blank=True, null=True)
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    postobrab = models.BooleanField(default=False, blank=True, null=True)
    action_summ = models.BooleanField(default=False, blank=True, null=True)
    info = models.TextField(default='', blank=True, null=True)
    postobrab_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return 'Подкатегория %s' % self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"



class Item(models.Model):
    sub_cat = models.ForeignKey(SubCat, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    number_pp = models.IntegerField(default=1, blank=True, null=True)
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    info = models.TextField(default='', blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return 'Свойство\Товар %s' % self.name

    class Meta:
        verbose_name = "Свойство\Товар"
        verbose_name_plural = "Свойства\Товары"
