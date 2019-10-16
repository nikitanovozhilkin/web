from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .managers import PostManager, PostPublishedManager


class Post(models.Model):
    """Django data model Post"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostManager()
    published = PostPublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def is_publish(self):
        return True if self.published_date else False

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Записи в блоге'

    def __str__(self):
        return self.title
