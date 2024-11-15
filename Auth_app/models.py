from django.db import models
from django.contrib.auth.models import User
import string
import random

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField(max_length=100)
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.user


