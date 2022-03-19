from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)
    text = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.author} {self.slug} {self.text}'
