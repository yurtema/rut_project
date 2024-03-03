from django.db import models

class Cinema_events(models.Model):
    title = models.CharField(max_length=50)
    afisha = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    # poster = models.ImageField(upload_to='posters/')
    # images = models.ManyToManyField('Image', related_name='movies')
    author = models.CharField(max_length=100, blank=True, null=True)
    participants = models.CharField(max_length=150, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    original_name = models.CharField(max_length=50, blank=True, null=True)

    def images_list(self):
        return self.images.split(',') if self.images else []

    def __str__(self):
        return self.title
