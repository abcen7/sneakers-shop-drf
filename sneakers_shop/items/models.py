from django.db import models


class Item(models.Model):
    image_path = models.ImageField(upload_to='media/', null=True, blank=True)
    title = models.CharField(max_length=255)
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title