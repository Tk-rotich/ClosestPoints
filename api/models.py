from django.db import models

# Create your models here.
class ClosestPoints(models.Model):
    points = models.TextField()
    closest = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.points)