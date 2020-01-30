from datetime import datetime

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class BlogPage(Page):
    intro = models.CharField(max_length=100)
    description = models.TextField()
    edited = models.DateTimeField(auto_now=datetime.now)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        posts = self.get_children().live().order_by('-first_published_at')
        context['posts'] = posts
        return context


class PostPage(Page):
    intro = models.TextField(max_length=300, blank=True)
    body = RichTextField(blank=True)
    created = models.DateTimeField(auto_now_add=datetime.now)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full")
    ]

    def get_absolute_url(self):
        return self.url
