from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic, related_name="news")
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="news"
    )

    class Meta:
        verbose_name_plural = "news"
        ordering = ["-publish_date"]

    def __str__(self):
        return f"{self.title} {self.publish_date}"


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return self.username
