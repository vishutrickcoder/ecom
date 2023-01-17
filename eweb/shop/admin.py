from django.contrib import admin
from .models import Product,Order
# Register your models here.

admin.site.site_header = "E-Commerse Web App"
admin.site.site_title = "E-comm Web"
admin.site.index_title = "Managing E-com Orders and Products"

class ProductsAdmin(admin.ModelAdmin):

    def change_default(self,request,queryset):
        queryset.update(category="default")

    list_display = ("title","price","discount_price","category","description")
    search_fields = ("title","category")
    actions = ("change_default",)
    list_editable = ("price","category")

admin.site.register(Product,ProductsAdmin)
admin.site.register(Order)