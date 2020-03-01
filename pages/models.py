from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        # null=True
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('page_detail', args=[str(self.id)])

