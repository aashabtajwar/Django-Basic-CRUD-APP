from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title