from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    body = models.TextField()

    def __str__(self):
        return self.title
