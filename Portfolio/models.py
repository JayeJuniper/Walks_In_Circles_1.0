from django.db import models
from django.utils import timezone


class Photo(models.Model):
    image = models.ImageField(upload_to='images/', default='')
    subject = models.CharField(max_length=50, blank=True, default='')
    caption = models.CharField(max_length=255, blank=True, default='')
    article_id = models.CharField(max_length=50, blank=True, default='')
    expedition_id = models.CharField(max_length=50, blank=True, default='')
    tags = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    text = models.TextField(max_length=500, blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    article_id = models.CharField(max_length=50, blank=True, default='')
    expedition_id = models.CharField(max_length=50, blank=True, default='')
    tags = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Expedition(models.Model):
    expedition_name = models.CharField(max_length=50, blank=True, default='')
    expedition_id = models.CharField(max_length=50, blank=True, default='')
    expedition_image = models.ImageField(upload_to='images/', default='')
    description = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Jeep(models.Model):
    jeep_name = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='images/', default='')
    history = models.TextField(max_length=500, blank=True, default='')
    specs = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    profile_pic = models.ImageField(upload_to='images/', default='')
    resume_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True, default='')
    certification_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True, default='')
    introduction = models.TextField(max_length=500, blank=True, default='')
    about = models.TextField(max_length=500, blank=True, default='')
    education_1 = models.TextField(max_length=500, blank=True, default='')
    education_2 = models.TextField(max_length=500, blank=True, default='')


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name