from django.contrib import admin
from .models import *


class SubCatInline (admin.TabularInline):
    model = SubCat
    extra = 0


class MainCatAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in MainCat._meta.fields]
    inlines = [SubCatInline]
    # exclude = ['for_squad','created_at','updated_at'] #не отображать на сранице редактирования
    class Meta:
        model = MainCat


class ItemsInline (admin.TabularInline):
    model = Item
    extra = 0

class SubCatAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in SubCat._meta.fields]
    inlines = [ItemsInline]
    # exclude = ['for_squad','created_at','updated_at'] #не отображать на сранице редактирования
    class Meta:
        model = SubCat


admin.site.register(MainCat, MainCatAdmin)
admin.site.register(Item)
admin.site.register(SubCat, SubCatAdmin)

