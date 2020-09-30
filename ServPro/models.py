from django.db import models
from django.contrib.auth.models import User


class service(models.Model):
    Service_Name = models.CharField(max_length=50)
    Service_Description = models.TextField()
    Charges = models.CharField(max_length=50)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Service_Name