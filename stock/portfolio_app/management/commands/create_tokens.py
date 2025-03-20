from django.core.management.base import BaseCommand 
from portfolio_app.models import CustomUser
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = "create tokens for all logedin users"

    def handle(self, *args , **kwargs):
        all_users = CustomUser.objects.all()
        for user in all_users:
            Token.objects.get_or_create(user = user)
        