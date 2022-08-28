from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customers','product', 'quantity','Order_status','Order_date','Price']
# Register your models here.
admin.site.register(Order, OrderAdmin)


# Register your models here.
