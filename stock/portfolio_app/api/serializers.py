from rest_framework import serializers as slzs
from portfolio_app.models import Stock,Broker,Portfolio,StockOrder

class StockSerial(slzs.ModelSerializer):
    # modify the output of serilaizer.data ----------------------------------------
    def to_representation(self, instance):
        '''GET
        this function is called to modify the output of serilaizer.data 
        after getting data from model
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
        print("data printed here first")
        return data
    # ------------------------------------------------------------------------------

    class Meta:
        model = Stock
        fields = "__all__"

class BrokerSerial(slzs.ModelSerializer):
    rbi_id = slzs.SerializerMethodField(required = False)

    # get custom field data dependent on another field -------------------
    def get_rbi_id(self,obj):
        str = obj.dmt_id
        str = str.split('-')[-1]
        return str
    #---------------------------------------------------------------------
    class Meta:
        model = Broker
        fields = "__all__"

class PortfolioSerial(slzs.ModelSerializer):
    # same name as related_name to get all data (not only id)
    broker = BrokerSerial(read_only = True) # <many = True> will return error if or if not reequired 
    # stocks = StockSerial(read_only = True) # not working for ManyToMany
    
    def to_representation(self,instance):
        data = super().to_representation(instance)
        print(type(data.get("stock_list","no stocs")))
        stock_id_list = data.get("stock_list",[])[:] # field is in many to many relation
        data["stock_list"] = StockSerial(
            Stock.objects.filter(id__in = stock_id_list),
            many = True
        ).data
        return data
    
    class Meta:
        model = Portfolio
        fields = "__all__"

# custom serializer
class StockOrderSerial(slzs.Serializer):
    # Dealing with nested objects
    portfolio = PortfolioSerial()
    stock = StockSerial()
    count = slzs.IntegerField(default = 0,required = False)
    # use good django ORMS
    def create(self,validated_data):
        pass

    def update(self,obj,input_data):
        return obj

    def save(self):
        self.validated_data["portfolio"]
        pass
    #---------------------------------------------------------------------