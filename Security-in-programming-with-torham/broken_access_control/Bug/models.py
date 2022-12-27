from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

ACCESS_LEVELS = (
    ("h", "higth"),
    ("m", "middle"),
    ("l", "Low"),
)

class Admins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=4 ,choices=ACCESS_LEVELS, default="l")


    def __str__(self) -> str:
        return f"{self.user.username} | {self.access_level}"
    
    @property
    def username(self):
        return self.user.username