from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.contrib.auth.models import Group


class User(AbstractUser):
    id = models.IntegerField(db_column='UserId', primary_key=True)
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return '<User {}>'.format(self.email)


Group.add_to_class('location', models.CharField(
    max_length=180, null=True, blank=True))
