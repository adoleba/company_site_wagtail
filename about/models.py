from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class About(Page):
    title_description = models.CharField(max_length=500)
    red_intro = models.TextField()
    black_intro = models.TextField()
    intro_description = models.TextField()
    first_offer = models.CharField(max_length=500)
    first_offer_description = models.TextField()
    second_offer = models.CharField(max_length=500)
    second_offer_description = models.TextField()
    third_offer = models.CharField(max_length=500)
    third_offer_description = models.TextField()
    first_step = models.CharField(max_length=500)
    first_step_description = models.TextField()
    second_step = models.CharField(max_length=500)
    second_step_description = models.TextField()
    third_step = models.CharField(max_length=100)
    third_step_description = models.TextField()
    summary_description = models.CharField(max_length=200)
    summary_first = models.CharField(max_length=100)
    summary_first_description = models.TextField()
    summary_second = models.CharField(max_length=100)
    summary_second_description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('title_description', classname="full"),
        FieldPanel('red_intro', classname="full"),
        FieldPanel('black_intro', classname="full"),
        FieldPanel('intro_description', classname="full"),
        FieldPanel('first_offer', classname="full"),
        FieldPanel('first_offer_description', classname="full"),
        FieldPanel('second_offer', classname="full"),
        FieldPanel('second_offer_description', classname="full"),
        FieldPanel('third_offer', classname="full"),
        FieldPanel('third_offer_description', classname="full"),
        FieldPanel('first_step', classname="full"),
        FieldPanel('first_step_description', classname="full"),
        FieldPanel('second_step', classname="full"),
        FieldPanel('second_step_description', classname="full"),
        FieldPanel('third_step', classname="full"),
        FieldPanel('third_step_description', classname="full"),
        FieldPanel('summary_description', classname="full"),
        FieldPanel('summary_first', classname="full"),
        FieldPanel('summary_first_description', classname="full"),
        FieldPanel('summary_second', classname="full"),
        FieldPanel('summary_second_description', classname="full"),
    ]
