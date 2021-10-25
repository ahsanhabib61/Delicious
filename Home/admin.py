from django.contrib import admin
from Home.models import Pizza , Burger ,Shawarma_pltr , Appetizer , Sandwiche , Pasta_Roll ,Address ,Customer ,Worker ,Cart,Cartitem,Order , Contact

# Register your models here.

admin.site.register(Contact )

admin.site.register(Pizza )
admin.site.register(Burger)
admin.site.register(Shawarma_pltr)
admin.site.register(Appetizer)
admin.site.register(Sandwiche)
admin.site.register(Pasta_Roll)

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(Order)

