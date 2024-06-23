from django.contrib import admin
from .models import Catagory, Order, Product, Store, Top_product,Cart,Wishlist,O_tracker,O_item

# Register your models here.
admin.site.register(Store)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Top_product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(O_tracker)
admin.site.register(Order)
admin.site.register(O_item)

