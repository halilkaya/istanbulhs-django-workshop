from __future__ import unicode_literals
from django.db import models
from django.contrib import auth

class Web(models.Model):
    """
    Web project for base page
    """
    TYPES = (
        ('wiki', 'Wiki Page'),
        ('general', 'Generic Page Type'),
        ('personal', 'My Custom Personal Content'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('auth.User', related_name='author')
    content_type = models.CharField(max_length=8, choices=TYPES, default='general')
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
