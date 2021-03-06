# Generated by Django 2.1.4 on 2019-04-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True, verbose_name='Ф.И.О.')),
                ('firm', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Организация')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(default='', max_length=50, null=True, verbose_name='Телефон')),
                ('firm_address', models.TextField(blank=True, default='', null=True, verbose_name='Адрес организации')),
                ('personal_address', models.TextField(blank=True, default='', null=True, verbose_name='Личный адрес')),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='Комментарий к клиенту')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
