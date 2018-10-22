from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 160)
    text = models.TextField()
    created = models.DateTimeField(default= timezone.now())
    published = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("posts_detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('blog_app.Posts',on_delete=models.CASCADE,related_name="comments")
    author = models.CharField(max_length = 80)
    text = models.TextField()
    created = models.DateTimeField(default= timezone.now())

    def get_absolute_url(self):
        return reverse("posts_list")

    def __str__(self):
        return self.text
