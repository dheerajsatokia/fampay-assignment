from django.db import models


class VideoDetail(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    high_thumbnail = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    publishedAt = models.CharField(max_length=125, null=True, blank=True)
    default_thumbnail = models.CharField(max_length=250, null=True, blank=True)
    medium_thumbnail = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class ApiKey(models.Model):
    secret = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.secret
