from django.db import models

class Theatre_events(models.Model):
    title = models.CharField(max_length=100)
    afisha = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    customer = models.TextField(blank=True, null=True)
    participants = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)

    def images_list(self):
        return self.images.split(',') if self.images else []

    def __str__(self):
        return self.title
