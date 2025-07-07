from django.db import models

# Create your models here.

class Recipe(models.Model):
    cuisine = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)
    prep_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)
    total_time = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    nutrients = models.JSONField(null=True, blank=True)  # Requires MySQL 5.7+
    serves = models.CharField(max_length=100)

    def __str__(self):
        return self.title
