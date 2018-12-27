from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    name = models.CharField(_('Имя'), max_length=50, blank=True, null=True, default='')
    family = models.CharField(_('Фамилия'), max_length=50, blank=True, null=True, default='')
    otchesnvo = models.CharField(_('Отчество'), max_length=50, blank=True, null=True, default='')
    firm = models.CharField(_('Фирма'), max_length=50, blank=True, null=True, default='')
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('Телефон'), max_length=50, blank=True, null=True, default='')
    is_vip = models.BooleanField(_('Вип'), default=False)
    firm_address = models.TextField(_('Адрес фирмы'),default='', blank=True, null=True)
    personal_address = models.TextField(_('Личный адрес'), default='', blank=True, null=True)
    
    
    def __str__(self):
        return 'Клиент :  %s %s %s' % (self.name, self.family, self.otchesnvo)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
