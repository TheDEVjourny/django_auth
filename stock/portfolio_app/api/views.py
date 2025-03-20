from rest_framework.decorators  import api_view , authentication_classes , permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from portfolio_app.models import Stock,Broker,Portfolio,StockOrder
from portfolio_app.api.serializers import StockSerial, BrokerSerial, PortfolioSerial#, StockOrderSerial
#----------------utility------------------------------------------
def get_data(
        model,
        serializer,
        name = None,
        custom_query = None
    ):
    '''the function will convert database response in to json/dict response'''
    # get query
    if name:
        query = model.objects.filter(name__iexact = name)
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

def set_data(input_data,serializer,extra_data = {}):
    '''the function will convert json/dict response in to database response'''
    try:
        seril = serializer(data = input_data)
        proceed = seril.is_valid()
        error = seril.error
    except:
        error = "issue in data serialization"
    return seril.save(extra_data) if proceed else {"error":error}
    

#--------------------------------------------------------------------

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def stock_data(request, name = None):
    '''Get the stock data from the database'''
    return Response(
        get_data(Stock,StockSerial,name), 
        status=200
    )


@api_view(["GET"])
def broker_data(request, name = None):
    '''Get the stock data from the database'''
    return Response(
         get_data(Broker,BrokerSerial,name),
        status=200
    )

@api_view(["GET"])
def portfolio_data(request, name = None):
    return Response(
         get_data(Portfolio,PortfolioSerial,name),
        status=200
    )