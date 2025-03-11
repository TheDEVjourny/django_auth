from rest_framework import serializers as slzs
from portfolio_app.models import Stock,Broker,Portfolio,StockOrder

class StockSerial(slzs.ModelSerializer):
    
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

#     def insert(self,obj,input_data):
#         pass

#     def save(self):
#         pass
        # validated_data["portfolio"]