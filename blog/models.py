from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(
        upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_view = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return (f"{self.id} - {self.title}")

    def excerpt(self, num_words=4):
        return Truncator(self.content).words(num_words, truncate=' ...')

    # def get_absolute_url(self):
    #     return reverse('blog:single', kwargs={'pid': self.id})
