from django.db import models

from customuser.models import User

class Client(models.Model):
    name = models.CharField('Имя', max_length=50, blank=False, null=True, default='')
    family = models.CharField('Фамилия', max_length=50, blank=False, null=True, default='')
    otchesnvo = models.CharField('Отчество', max_length=50, blank=False, null=True, default='')
    firm = models.CharField('Организация', max_length=50, blank=True, null=True, default='')
    email = models.EmailField('email address', unique=True)
    phone = models.CharField('Телефон', max_length=50, blank=False, null=True, default='')
    firm_address = models.TextField('Адрес организации',default='', blank=True, null=True)
    personal_address = models.TextField('Личный адрес', default='', blank=True, null=True)
    comment = models.TextField('Комментарий к клиенту', default='', blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Ведущий менеджер')

    def __str__(self):
        return 'Клиент :  %s %s %s' % (self.name, self.family, self.otchesnvo)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
