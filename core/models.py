from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, username, email, is_buyer, is_seller, seller_name):
        user = self.model(
            username=username,
            email=email,
            is_buyer=is_buyer,
            is_seller=is_seller,
            seller_name=seller_name
        )
        user.save()
        return user

    def create_user(self, username, email, is_buyer, is_seller, seller_name):
        return self._create_user(username, email, is_buyer, is_seller, seller_name)

    def create_superuser(self, username, email, is_buyer, is_seller, seller_name):
        user = self._create_user(self, username, email, is_buyer, is_seller, seller_name)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length = 128,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    seller_name = models.CharField(max_length=100, default = '')
    password = None

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email
