from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogModel(models.Model):

    content = models.TextField()
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Images(models.Model):
    image_link = models.URLField()
    model = models.ForeignKey(
        BlogModel, on_delete=models.CASCADE, related_name="post_images")

    def __str__(self):
        return self.model.title
