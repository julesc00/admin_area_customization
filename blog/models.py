from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
