from django.contrib import admin
from portfolio_app.models import Stock,Broker,Portfolio,StockOrder,CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Stock)
admin.site.register(Broker)
admin.site.register(Portfolio)
admin.site.register(StockOrder)