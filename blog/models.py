from distutils.command import upload
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True, null=True)
    images = models.ImageField(null=True, blank=True, upload_to="uploads")
    created_date = models.DateTimeField(default=timezone.localtime)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.localtime()
        self.save()

    def get_absolute_url(self):
        # to redirect to a page after creating an object of the class
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.localtime())

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name="imagess")
    image = models.ImageField(upload_to='images/')

    def str(self):
        return self.post.title 