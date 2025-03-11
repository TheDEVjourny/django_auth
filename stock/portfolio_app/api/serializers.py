from rest_framework import serializers as slzs
from portfolio_app.models import Stock,Broker,Portfolio,StockOrder

class StockSerial(slzs.ModelSerializer):
    # this function is called to modify the output of serilaizer.data after getting data from model
    def to_representation(self, instance):
        '''GET
        instance : model object or model object list
        '''
        # data : serialized model data 
        data  = super().to_representation(instance)
        # data addition in serialized data
        data["stocl_order_status"]= "sold"
        return data

    # the post data will first come here as data before validation
    def to_internal_value(self,data):
        """POST
        data: data before validation
        """
        # process data to make it validable data
        return data

    class Meta:
        model = Stock
        fields = "__all__"

class BrokerSerial(slzs.ModelSerializer):
    
    class Meta:
        model = Broker
        fields = "__all__"

class PortfolioSerial(slzs.ModelSerializer):
    
    class Meta:
        model = Portfolio
        fields = "__all__"

# custom serializer
# class StockOrderSerial(slzs.Serializer):
#     # Dealing with nested objects
#     portfolio = PortfolioSerial()
#     stock = StockSerial()
#     count = slzs.IntegerField(default = 0)

#     def create(self,validated_data):
#         pass

#     def update(self,obj,input_data):
#         pass

#     def save(self):
#         pass
        # validated_data["portfolio"]