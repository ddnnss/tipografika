from django.db import models
from client.models import Client
from customuser.models import User




class Order(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Клиент')
    total_price = models.DecimalField('Стоимость заказа', max_digits=8, decimal_places=2, blank=True, null=True)
    order_received = models.DateTimeField('Дата принятия заказа', blank=True, null=True)
    is_vip = models.BooleanField('Вип заказ', default=False)
    comment = models.TextField('Коментарий', default='', blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True,verbose_name='Ведущий менеджер', on_delete=models.SET_NULL)
    is_money_received = models.BooleanField('Статус оплаты', default=False)
    is_manager_pay = models.BooleanField('Выплата менеджеру', default=False)
    is_complete = models.BooleanField('Заказ выполнен', default=False)
    order_all_time = models.DateTimeField('Срок сдачи заказа', blank=True, null=True)
    deadline = models.DateTimeField('Дата сдачи заказа', blank=True, null=True)
    delivery_address = models.TextField('Доставка заказа', default='', blank=True, null=True)


    def __str__(self):
        return 'Заказ №:  %s ' % self.id

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Status(models.Model):
    name = models.CharField('Название статуса', max_length=50, blank=False)



    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class ItemsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='В заказе')
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Статус')
    item_info = models.TextField('Содержание позиции', default='', blank=True, null=True)
    tirag = models.IntegerField('Тираж', default=0, blank=True, null=True)
    comment = models.TextField('Коментарий', default='', blank=True, null=True)
    order_all_time = models.DateTimeField('Срок сдачи ', blank=True, null=True)
    deadline = models.DateTimeField('Дата сдачи ', blank=True, null=True)
    price = models.DecimalField('Стоимость позиции', max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return 'Позиция в заказе №:  %s ' % self.order.id

    class Meta:
        verbose_name = "Позиция в заказе"
        verbose_name_plural = "Позиции в заказах"