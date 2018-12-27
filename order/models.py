from django.db import models
from django.utils.translation import ugettext_lazy as _
from client.models import Client
from products.models import Item
from customuser.models import User




class Order(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, blank=True,related_name='manager', null=True, on_delete=models.SET_NULL)
    performer = models.ForeignKey(User, blank=True, related_name='performer', null=True, on_delete=models.SET_NULL)
    total_price = models.DecimalField(_('Стоимость заказа'), max_digits=8, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(_('Скидка'), default=0, blank=True, null=True)
    tirag = models.IntegerField(_('Тираж'), default=0, blank=True, null=True)
    comment = models.TextField(_('Коментарий'), default='', blank=True, null=True)
    maket = models.ImageField(_('Макет'), upload_to='orders/', null=True, blank=True)
    dead_time = models.DateTimeField(_('Срок выполнения'), blank=True, null=True)
    is_vip = models.BooleanField(_('Вип заказ'), default=False)
    delivery = models.BooleanField(_('Доставка'), default=False)
    delivery_address = models.TextField(_('Адрес доставки'), default='', blank=True, null=True)


    def __str__(self):
        return 'Заказ №:  %s ' % self.id

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ItemsInOrder(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Товар в заказе №:  %s ' % self.order.id

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказах"