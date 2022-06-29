from django.db import models


# Create your models here.

class BlogModel(models.Model):
    author = models.CharField('author', max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.author
