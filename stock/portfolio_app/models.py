from django.db import models

# class User(models.Model):
#     pass

class Stock(models.Model):
    stock_name = models.CharField(max_length = 200)
    nse_id = models.CharField(max_length = 500, unique = True)
    count =  models.IntegerField(default = 0)
    about = models.JSONField()


class Broker(models.Model):
    broker_name = models.CharField(max_length = 200)
    dmt_id = models.CharField(max_length = 200,unique = True)

class Portfolio(models.Model):
    # user =  models.ForeignKey(USER, on_delete = models.PROTECT)
    broker = models.ForeignKey(Broker, on_delete = models.CASCADE)
    stock_list = models.ManyToManyField(Stock)
    custom_algo = models.TextField()


