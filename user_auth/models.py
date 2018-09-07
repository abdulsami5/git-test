from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    """This is the User model to represent User entity"""
    uuid = models.UUIDField(unique=True,default=uuid.uuid4, editable=False, primary_key=True)
    profile_pic = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        """This function is to get representation of User model"""
        return self.email
