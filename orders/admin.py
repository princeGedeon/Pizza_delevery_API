from django.contrib import admin

# Register your models here.
from orders.models import Orders


@admin.register(Orders)
class orderAdmin(admin.ModelAdmin):
    list_display = ["size","order_status","quantity","customer","created_at"]
    list_filter = ["created_at","order_status"]
