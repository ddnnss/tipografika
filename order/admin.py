from django.contrib import admin
from .models import *



class OrderItemsInline (admin.TabularInline):
    model = ItemsInOrder
    extra = 0




class OrderAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderItemsInline]
    # exclude = ['for_squad','created_at','updated_at'] #не отображать на сранице редактирования
    class Meta:
        model = Order





admin.site.register(Order, OrderAdmin)
