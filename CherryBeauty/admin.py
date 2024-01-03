
from django.contrib import admin
from .models import Comment,Customer, Order, Post,Collection,Brand,Nation,Product, ShippingAddress,Tag,OderItem,Like


class PostAdmin(admin.ModelAdmin):
   list_display = ('id','title','header_image') 
admin.site.register(Post,PostAdmin)


admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Nation)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(Tag,ProductAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','collection','price','is_sell')
    list_editable = ('is_sell',)
admin.site.register(Product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','phone_number')
admin.site.register(Customer,CustomerAdmin)

admin.site.register(Order)
admin.site.register(OderItem)
admin.site.register(ShippingAddress)
admin.site.register(Like)
admin.site.register(Comment)
