from rest_framework.decorators  import api_view
from rest_framework.response import Response

from portfolio_app.models import Stock,Broker,Portfolio,StockOrder
from portfolio_app.api.serializers import StockSerial, BrokerSerial, PortfolioSerial#, StockOrderSerial



@api_view(["GET"])
def stock_data(request, name = None):
    # Get the stock data from the database
    stocks = None
    if not name:
        stocks = Stock.objects.all()
    else:
        stocks = Stock.objects.filter(name = name)

    serializer = StockSerial(stocks ,many = True)
    return Response(serializer.data , status=200)