from django.db import models

from django.contrib.auth.models import User
from django.db import IntegrityError


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    scheduled_time = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if (self.project.user.id == self.user.id):
            super(Event, self).save(*args, **kwargs)
        else:
            raise IntegrityError



class Comment(models.Model):
    content = models.CharField(max_length=3000)
    post_time = models.DateTimeField(auto_now=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

