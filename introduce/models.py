from django.db import models

# Create your models here.
class AccessLog(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.create_at} / {self.location}"