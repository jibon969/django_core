from django.db import models
from blog.models import Blog
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    approve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Replay(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replays')
    body = models.TextField()
    approve = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)

