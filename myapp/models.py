from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name  # Added for consistency with the Skill model

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title  # Only one __str__ method
