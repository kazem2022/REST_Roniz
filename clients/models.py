from django.db import models

# Create your models here.

class Client(models.Model):
    user_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11) # remember that phone number is string, because of '+','-'
    description = models.TextField()

    def __str__(self):
        return self.user_id