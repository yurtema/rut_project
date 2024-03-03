from django.db import models

class Concert_events(models.Model):
    title = models.CharField(max_length=50)
    afisha = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)

    def images_list(self):
        return self.images.split(',') if self.images else []

    def __str__(self):
        return self.title