from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import uuid
from django.utils import timezone

class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email