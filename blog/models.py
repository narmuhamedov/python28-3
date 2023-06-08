from django.db import models


class Blog(models.Model):
    title_blog = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="")
    description = models.TextField()
    type_blog = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_blog
