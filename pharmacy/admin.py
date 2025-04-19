from django.contrib import admin
from .models import Medicine, Customer, Sale, SaleItem

admin.site.register(Medicine)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleItem)