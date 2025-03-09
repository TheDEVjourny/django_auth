from django.db import models
from django.core.exceptions import ValidationError

#---validator--------------
def validate_id(value):
    if len(value) > 3:
        return True
    else:
        # raise Exception("bad") # tool broken
        raise ValidationError('bad')

def stock_count(value):
    # validation not working
    return True if value>=1 else False 
#--------------------------


class Stock(models.Model):
    name = models.CharField(max_length = 200)
    nse_id = models.CharField(max_length = 500, unique = True)
    about = models.JSONField()

    def __str__(self):
        return self.name 

class Broker(models.Model):
    name = models.CharField(max_length = 200)
    dmt_id = models.CharField(
        max_length = 200,
        unique = True,
        validators = [validate_id]
        )
    
    def __str__(self):
        return self.name



class Portfolio(models.Model):
    name = models.CharField(max_length = 100,default= "NULL")
    # user =  models.ForeignKey(USER, on_delete = models.PROTECT)
    broker = models.ForeignKey(Broker, on_delete = models.CASCADE)
    stock_list = models.ManyToManyField(Stock)
    custom_algo = models.TextField()

    def __str__(self):
        return self.name


class StockOrder(models.Model):
    portfolio = models.ForeignKey(Portfolio , on_delete = models.CASCADE)
    stock = models.ForeignKey(Stock , on_delete = models.CASCADE)
    count =  models.IntegerField(default = 0, validators = [stock_count])
    # not able to identify is stock present in portfolio or not
    def __str__(self):
        return f"order:{self.portfolio.name}-{self.stock.name}-{self.count}"