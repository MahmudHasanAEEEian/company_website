from django.db import models

# Create your models here.
class SendMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    