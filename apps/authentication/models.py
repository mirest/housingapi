from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .token_generator import get_tokens_for_user as get_token


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone']

    class Meta:
        db_table = 'User'

    def __str__(self):
        return '<User {}>'.format(self.email)

    def token(self):
        return get_token(self)
