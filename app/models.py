from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=[
        ('vendor', 'Vendor'),
        ('businessman', 'Businessman'),
        ('person', 'Person'),
    ])

    def __str__(self):
        return self.user.username
