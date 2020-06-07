from django.db import models

# Create your models here.

class Blog(models.Model):
    title_blog = models.CharField(max_length=200)
    description_blog = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.title_blog