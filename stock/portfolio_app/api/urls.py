from django.urls import path
from portfolio_app.api.views import stock_data,broker_data,portfolio_data

urlpatterns = [
    path("stocks/",stock_data),
    path("stocks/<str:name>",stock_data),
    path("brokers/",broker_data),
    path("brokers/<str:name>",broker_data),
    path("Portfolios/",portfolio_data),
    path("Portfolios/<str:name>",portfolio_data)
]