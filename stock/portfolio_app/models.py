from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import random , string
# custom user-------------------------------------

class CustomUserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        # username = self.normalize_username(username)
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password) # pass word hasing faild ??
        user.save(using=self._db) 
        return user

    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_manager", True)
        extra_fields.setdefault("is_employee", False)
        return self.create_user(username,password,**extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,unique = True)
    location = models.TextField()
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    # in_groups = models.JSONField(default = {})
    # user_id -> error
    custom_id = models.CharField(
        max_length=300, 
        default = ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
        unique = True
        )
    
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email","location"]


#-------------------------------------------------

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
    user =  models.ForeignKey(get_user_model(), on_delete = models.PROTECT)
    broker = models.ForeignKey(Broker,related_name= "broker", on_delete = models.CASCADE)
    stock_list = models.ManyToManyField(Stock,related_name= "stocks") # related name give no impact
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