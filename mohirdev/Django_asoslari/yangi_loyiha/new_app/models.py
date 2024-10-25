from django.utils import timezone
from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISHED)


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class News(models.Model):
    # UUID = models.UUIDField(primary_key=True, unique=True) # Bu ID ni ko'p Xonalik qiladi
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT
                              )
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish_time',) #-published_time'

    def __str__ (self):
        return self.title

