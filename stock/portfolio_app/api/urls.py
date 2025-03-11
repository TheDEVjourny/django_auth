from django.urls import path
from portfolio_app.api.views import stock_data

urlpatterns = [
    path("stocks/",stock_data),
    path("stocks/<str:name>",stock_data)
]