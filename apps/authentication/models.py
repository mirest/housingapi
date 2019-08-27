from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField('LandLord', default=True,)

    def __str__(self):
        return '<User {}>'.format(self.email)
