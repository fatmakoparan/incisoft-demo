from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
