from django.db import models
from  django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Custom manager to filter post according to the status based on published
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    body = models.TextField(_('Body'))
    author = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='blog_post'
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(_('STATUS'),
                                max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')


    objects = models.Manager() # default query Manager
    published = PublishedManager() # Custom Manager

    class Meta:
        # ordering of post in the database
        ordering = ('-publish',)


    def __repr__(self):
        # display of post when quering in the shell
        # display post by title when queried
        return f'{self.title!r}'
