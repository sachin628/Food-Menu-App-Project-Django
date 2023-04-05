from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item
        fields = ['item_id', 'item_name','item_desc','item_price']
