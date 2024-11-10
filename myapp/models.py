from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this field exists

    def __str__(self):
        return self.title

class List_Category(models.Model):
    project = models.ForeignKey(Project, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
