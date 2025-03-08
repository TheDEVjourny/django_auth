from django.contrib import admin
from portfolio_app.models import Stock,Broker,Portfolio
# Register your models here.
admin.site.register(Stock)
admin.site.register(Broker)
admin.site.register(Portfolio)