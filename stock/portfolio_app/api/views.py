from rest_framework.decorators  import api_view
from rest_framework.response import Response

from portfolio_app.models import Stock,Broker,Portfolio,StockOrder
from portfolio_app.api.serializers import StockSerial, BrokerSerial, PortfolioSerial#, StockOrderSerial
#----------------utility------------------------------------------
def get_json_data(
        model,
        serializer,
        name = None,
        custom_query = None
    ):
    '''the function will convert database response in to json/dict response'''
    # get query
    if name:
        query = model.objects.filter(name=name)
    elif custom_query:
        try:
            query = custom_query
        except:
            print("query is not correct")
    else:
        query = model.objects.all()
    # serialize query
    serial = serializer(query,many = True)
    # return json response
    return serial.data
#--------------------------------------------------------------------

@api_view(["GET"])
def stock_data(request, name = None):
    '''Get the stock data from the database'''
    return Response(
        get_json_data(Stock,StockSerial,name), 
        status=200
    )


@api_view(["GET"])
def broker_data(request, name = None):
    '''Get the stock data from the database'''
    return Response(
         get_json_data(Broker,BrokerSerial,name),
        status=200
    )

@api_view(["GET"])
def portfolio_data(request, name = None):
    return Response(
         get_json_data(Portfolio,PortfolioSerial,name),
        status=200
    )