# Generated by Django 2.1.4 on 2019-04-23 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_info', models.TextField(blank=True, default='', null=True, verbose_name='Содержание позиции')),
                ('tirag', models.IntegerField(blank=True, default=0, null=True, verbose_name='Тираж')),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='Коментарий')),
                ('order_all_time', models.DateTimeField(blank=True, null=True, verbose_name='Срок сдачи ')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Дата сдачи ')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Стоимость позиции')),
            ],
            options={
                'verbose_name': 'Позиция в заказе',
                'verbose_name_plural': 'Позиции в заказах',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Стоимость заказа')),
                ('order_received', models.DateTimeField(blank=True, null=True, verbose_name='Дата принятия заказа')),
                ('is_vip', models.BooleanField(default=False, verbose_name='Вип заказ')),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='Коментарий')),
                ('is_money_received', models.BooleanField(default=False, verbose_name='Статус оплаты')),
                ('is_manager_pay', models.BooleanField(default=False, verbose_name='Выплата менеджеру')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Заказ выполнен')),
                ('order_all_time', models.DateTimeField(blank=True, null=True, verbose_name='Срок сдачи заказа')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Дата сдачи заказа')),
                ('delivery_address', models.TextField(blank=True, default='', null=True, verbose_name='Доставка заказа')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.Client', verbose_name='Клиент')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Ведущий менеджер')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.AddField(
            model_name='itemsinorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order', verbose_name='В заказе'),
        ),
        migrations.AddField(
            model_name='itemsinorder',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Status', verbose_name='Статус'),
        ),
    ]
