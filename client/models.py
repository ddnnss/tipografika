from django.db import models

from customuser.models import Manager

class Client(models.Model):
    """Клиент"""
    name = models.CharField('Ф.И.О.', max_length=50, blank=False, null=True, default='')
    firm = models.CharField('Организация', max_length=50, blank=True, null=True, default='')
    email = models.EmailField('email address', unique=True)
    phone = models.CharField('Телефон', max_length=50, blank=False, null=True, default='')
    firm_address = models.TextField('Адрес организации',default='', blank=True, null=True)
    personal_address = models.TextField('Личный адрес', default='', blank=True, null=True)
    comment = models.TextField('Комментарий к клиенту', default='', blank=True, null=True)
    manager = models.ForeignKey(Manager, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Ведущий менеджер')

    def __str__(self):
        return 'Клиент :  %s ' % self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
