# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.db.models.signals import pre_save
# from blog.utils import blog_unique_slug_generator


# class Category(models.Model):
#     title = models.CharField(max_length=120)
#     slug = models.SlugField(null=True, blank=True, max_length=50)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['-timestamp']


# def category_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = blog_unique_slug_generator(instance)


# pre_save.connect(category_pre_save_receiver, sender=Category)


# class BlogManager(models.Manager):
#     def get_queryset(self):
#         return super(BlogManager, self).get_queryset() \
#             .filter(status='published')


# class Blog(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     body = models.TextField()
#     image = models.FileField(upload_to="blog", blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#     objects = models.Manager()  # The default manager.
#     published = BlogManager()  # Our custom manager.

#     def get_absolute_url(self):
#         return reverse(
#             'blog:post_detail',
#             args=[
#                 self.publish.year,
#                 self.publish.month,
#                 self.publish.day, self.slug
#             ])

#     class Meta:
#         ordering = ('-publish',)

#     def __str__(self):
#         return self.title


# # def blog_pre_save_receiver(sender, instance, *args, **kwargs):
# #     if not instance.slug:
# #         instance.slug = blog_unique_slug_generator(instance)
# #
# #
# # pre_save.connect(blog_pre_save_receiver, sender=Blog)


# class Comment(models.Model):
#     post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField(blank=True, null=True)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approve = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)


# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
#     name = models.CharField(max_length=80)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approve = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Reply {} by {}'.format(self.body, self.name)
